import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def run_prediction_pipeline(attendance_df, ia1_df, ia2_df):
    performance_df = pd.merge(ia1_df, ia2_df, on='Student_Name', suffixes=('_IA1', '_IA2'))
    master_df = pd.merge(performance_df, attendance_df, on='Student_Name')
    ia1_cols = [col for col in master_df.columns if '_IA1' in col and 'S.No' not in col]
    ia2_cols = [col for col in master_df.columns if '_IA2' in col and 'S.No' not in col]
    master_df['Average_IA_Score'] = (master_df[ia1_cols].mean(axis=1) + master_df[ia2_cols].mean(axis=1)) / 2
    master_df['Pass'] = ((master_df['Average_IA_Score'] >= 50) & (master_df['Attendance'] >= 75)).astype(int)
    features = ['Average_IA_Score', 'Attendance']
    target = 'Pass'
    X = master_df[features]
    y = master_df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred_test = model.predict(X_test)
    model_accuracy = accuracy_score(y_test, y_pred_test)
    master_df['Predicted_Pass'] = model.predict(X)
    final_output_df = master_df[['Student_Name', 'Predicted_Pass']]
    return final_output_df, master_df, model_accuracy
st.set_page_config(layout="wide")
st.title("🎓 AI-Powered Student Performance Predictor")
st.sidebar.header("Upload Your Data Files")
attendance_file = st.sidebar.file_uploader("Upload Attendance CSV", type=["csv", "xlsx"])
ia1_file = st.sidebar.file_uploader("Upload IA1 Performance CSV", type=["csv", "xlsx"])
ia2_file = st.sidebar.file_uploader("Upload IA2 Performance CSV", type=["csv", "xlsx"])
if st.sidebar.button("Run Prediction"):
    if attendance_file and ia1_file and ia2_file:
        with st.spinner('Processing data and training model...'): 
            try:
                attendance_df = pd.read_csv(attendance_file)
                ia1_df = pd.read_csv(ia1_file)
                ia2_df = pd.read_csv(ia2_file)
            except Exception:
                attendance_df = pd.read_excel(attendance_file)
                ia1_df = pd.read_excel(ia1_file)
                ia2_df = pd.read_excel(ia2_file)
            predictions_df, full_df, accuracy = run_prediction_pipeline(attendance_df, ia1_df, ia2_df)
            st.success('Prediction Complete!')
            st.subheader("Prediction Summary")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Model Accuracy", f"{accuracy:.2%}")             
                fig, ax = plt.subplots()
                sns.countplot(x='Predicted_Pass', data=full_df, hue='Predicted_Pass', palette=['#E74C3C', '#2ECC71'], legend=False, ax=ax)
                ax.set_title('Summary of Predicted Outcomes')
                ax.set_xticklabels(['Fail (0)', 'Pass (1)'])
                for container in ax.containers:
                    ax.bar_label(container)
                st.pyplot(fig)            
            with col2:
                st.write("Full Prediction List:")
                st.dataframe(predictions_df)
    else:
        st.sidebar.warning("Please upload all three required files.")
else:
    st.info("Upload your three data files in the sidebar and click 'Run Prediction' to begin.")
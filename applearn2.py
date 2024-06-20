import streamlit as st
import pandas as pd
import numpy as np

# Function to display chapter content
def show_chapter(chapter):
    if chapter == "Chapter One":
        st.subheader("1. CHAPTER ONE")
        with st.expander("1.1 Introduction"):
            st.write("""
            - This section provides an overview of the broader context of the study. 
            It discusses the historical, theoretical, and empirical foundations that led to the 
            formulation of the research topic. It sets the stage for the research by 
            explaining why the topic is important and relevant.
            """)
        with st.expander("1.2 Background of the Study"):
            st.write("""
            - This section clearly articulates the specific issue or gap in knowledge that 
            the research aims to address. It outlines the problem that motivated the study, 
            indicating the need for investigation and the potential impact of solving this problem.
            """)
        with st.expander("1.3 Purpose of the Study"):
            st.write("""
            - This section states the overall aim or intent of the research. 
            It describes what the study seeks to achieve, often framed as a broad statement that 
            outlines the main goal of the research project.
            """)
        with st.expander("1.4 Objective of the Study"):
            st.write("""
            - This section lists the specific, measurable goals that the research aims to accomplish. 
            Objectives are usually more detailed than the purpose and provide a clear roadmap for the research process.
            """)
        with st.expander("1.5 Research Questions"):
            st.write("""
            - This section presents the specific questions that the research seeks to answer. These questions guide 
            the study's focus and methodology, providing a clear direction for data collection and analysis.
            """)
        with st.expander("1.6 Significance of the Study"):
            st.write("""
            - This section explains the importance and potential impact of the research.
            """)
        with st.expander("1.7 Scope of the Study"):
            st.write("""
            - This section delineates the boundaries of the research. It defines the 
            parameters such as the geographical area, time frame, population, and specific 
            aspects of the topic that will be covered in the study, ensuring clarity 
            about what will and will not be included.
            """)
        with st.expander("1.8 Definition of Terms"):
            st.write("""
            - This section provides clear definitions of key terms and concepts used in the study. 
            It ensures that readers understand the specific meanings and context in which these 
            terms are used, avoiding ambiguity and enhancing comprehension.
            """)
    elif chapter == "Chapter Two":
        st.subheader("2. CHAPTER TWO")
        with st.expander("Review of Related Literature"):
            st.write("""
            - Overview of existing research or developments related to the project.
            """)
        with st.expander("2.1 Conceptual Framework"):
            st.write("""
            - Analysis of previous studies, projects, or products in the field.
            """)
        with st.expander("2.2 Theoretical Framework"):
            st.write("""
            - Relevant theories, models, or concepts that underpin the project.
            """)
        with st.expander("2.3 Empirical Review"):
            st.write("""
            - Analysis of empirical studies related to the project.
            """)
        with st.expander("2.4 Appraisal of Reviewed Literature"):
            st.write("""
            - Critical assessment of the reviewed literature and its relevance to the project.
            """)
    elif chapter == "Chapter Three":
        st.subheader("3. CHAPTER THREE")
        with st.expander("Research Methodology"):
            st.write("""
            **3.1 Area of Study**
            - Description of the geographical or thematic area where the study is conducted.
            """)
        with st.expander("3.2 Research Design"):
            st.write("""
            - Explanation of the overall research strategy and approach.
            """)
        with st.expander("3.3 Population of Study"):
            st.write("""
            - Information about the population or sample being studied.
            """)
        with st.expander("3.4 Sample and Sampling Technique"):
            st.write("""
            - Description of the sampling methods used to select participants.
            """)
        with st.expander("3.5 Instrument for Data Collection"):
            st.write("""
            - Details of the tools or instruments used to collect data.
            """)
        with st.expander("3.6 Validation of Instrument"):
            st.write("""
            - Methods used to validate the data collection instruments.
            """)
        with st.expander("3.7 Reliability of the Instrument"):
            st.write("""
            - Techniques used to ensure the reliability of the data collection instruments.
            """)
        with st.expander("3.8 Method of Data Collection"):
            st.write("""
            - Procedures and processes for collecting data from participants.
            """)
    elif chapter == "Chapter Four":
        st.subheader("4. CHAPTER FOUR")
        with st.expander("Result and Discussion"):
            st.write("""
            **4.1 Data Presentation and Analysis**
            - Presentation and analysis of the collected data.
            """)
        with st.expander("4.2 Discussion of Findings"):
            st.write("""
            - Interpretation and discussion of the research findings.
            """)
    elif chapter == "Chapter Five":
        st.subheader("5. CHAPTER FIVE")
        with st.expander("Summary, Conclusion and Recommendation"):
            st.write("""
            **5.1 Summary**
            - Summary of the research findings and key points.
            """)
        with st.expander("5.2 Conclusion"):
            st.write("""
            - Conclusion drawn from the research study.
            """)
        with st.expander("5.3 Recommendation"):
            st.write("""
            - Recommendations based on the research findings.
            """)
    elif chapter == "Reference":
        st.subheader("Reference")
        with st.expander("Academic Papers"):
            st.write("""
            - Citations of academic papers and articles referenced.
            """)
        with st.expander("Technical Documentation"):
            st.write("""
            - References to tools, libraries, and other technical resources.
            """)
        with st.expander("Additional Sources"):
            st.write("""
            - Any other relevant sources of information used.
            """)
    elif chapter == "Appendices":
        st.subheader("Appendices")
        with st.expander("Supplementary Materials"):
            st.write("""
            - Additional diagrams, charts, or documents supporting the project.
            """)
        with st.expander("Code Documentation"):
            st.write("""
            - Detailed documentation of the codebase, if applicable.
            """)
        with st.expander("User Manuals"):
            st.write("""
            - Instructions or manuals for using the developed system or product.
            """)

    # Interactive input for feedback
    feedback = st.text_area("Provide your feedback or additional comments here:")
    if st.button("Submit Feedback"):
        st.write("Thank you for your feedback!")

# Main function
def main():
    st.title("Final Year Project Outline")

    # Sidebar for chapter selection
    st.sidebar.title("Chapters")
    chapter = st.sidebar.radio("Select a Chapter", (
        "Chapter One", "Chapter Two", "Chapter Three", 
        "Chapter Four", "Chapter Five", 
        "Reference", "Appendices"))

    # Display the selected chapter content
    show_chapter(chapter)

if __name__ == "__main__":
    main()

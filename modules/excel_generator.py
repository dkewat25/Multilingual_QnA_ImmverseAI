import pandas as pd


def save_to_excel(translated_qna, filename="QnA.xlsx"):
    """
    Save QnA pairs into an Excel file with
    three sheets: English, Hindi, Marathi
    """

    english_data = []
    hindi_data = []
    marathi_data = []

    for qna in translated_qna:

        english_data.append({
            "Questions": qna["question_en"],
            "Answers": qna["answer_en"]
        })

        hindi_data.append({
            "Questions": qna["question_hi"],
            "Answers": qna["answer_hi"]
        })

        marathi_data.append({
            "Questions": qna["question_mr"],
            "Answers": qna["answer_mr"]
        })

    df_en = pd.DataFrame(english_data)
    df_hi = pd.DataFrame(hindi_data)
    df_mr = pd.DataFrame(marathi_data)

    with pd.ExcelWriter(filename) as writer:

        df_en.to_excel(writer, sheet_name="English", index=False)
        df_hi.to_excel(writer, sheet_name="Hindi", index=False)
        df_mr.to_excel(writer, sheet_name="Marathi", index=False)

    print(f"\nExcel file saved as {filename}")
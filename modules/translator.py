from googletrans import Translator

translator = Translator()


def translate_qna(qna_pairs):
    """
    Translate QnA pairs into Hindi and Marathi
    """

    translated_data = []

    for qna in qna_pairs:

        question_en = qna["question"]
        answer_en = qna["answer"]

        # Hindi
        question_hi = translator.translate(question_en, dest="hi").text
        answer_hi = translator.translate(answer_en, dest="hi").text

        # Marathi
        question_mr = translator.translate(question_en, dest="mr").text
        answer_mr = translator.translate(answer_en, dest="mr").text

        translated_data.append({
            "question_en": question_en,
            "answer_en": answer_en,
            "question_hi": question_hi,
            "answer_hi": answer_hi,
            "question_mr": question_mr,
            "answer_mr": answer_mr
        })

    return translated_data
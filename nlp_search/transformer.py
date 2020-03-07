from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
import torch

def question_transformer(question, context, attempt):
    context_list = [c for c in context.split('\n') if len(c) > 1]
    if len(context_list) - 1 < attempt:
        return None

    context = context_list[attempt]

    tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
    model = AutoModelForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")

    inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]

    text_tokens = tokenizer.convert_ids_to_tokens(input_ids)
    answer_start_scores, answer_end_scores = model(**inputs)

    answer_start = torch.argmax(
        answer_start_scores
    )  # Get the most likely beginning of answer with the argmax of the score
    answer_end = torch.argmax(answer_end_scores) + 1  # Get the most likely end of answer with the argmax of the score

    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))

    return answer

def sentiment_transformer(text):
    nlp = pipeline("sentiment-analysis")
    return nlp(text)[0].get('label')
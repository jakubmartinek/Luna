from main_cluster_pattern import *
from subj_neuron_net import *
import openai
import json

openai.api_key = "" #Tady nemůžu napsat api key , protože je placený

counter = 0
sleep_data = []
data_name = ["usnutí ", "vzbuzení ", "délka spánku ", "lehký spánek ", "hluboký spánek ", "REM ", "počet probuzení "]

print(f"Write data: usnutí, vzbuzení, délka spánku, lehký spánek, hluboký spánek, REM, počet probuzení")
for _ in range(7):
    sleep_data_input = int(input(data_name[counter]))
    sleep_data.append(sleep_data_input)
    counter += 1
subj_input = int(input("subjective sleep rate "))

bd_sleep = []
counter = 0

ranges = [(1295, 1395), (308, 408), (363, 463), (146, 246), (80, 165), (90, 150), (2, 0)]
for inf, (lower, upper) in zip(sleep_data, ranges):
    if lower <= inf <= upper:
        counter += 1
    else:
        bd_sleep.append(data_name[counter])
        counter += 1

if bd_sleep:
    prompt_res = f"Potřebuji pomoc se spánkem, můj spánek je podprůměrný v oblastech: {bd_sleep}"
else:
    prompt_res = "Mám dobrý spánek."

chatgpt_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt_res},
    ],
)

response_to_str = json.dumps(chatgpt_response)

final_answer = chatgpt_response["choices"][0]["message"]["content"]

if not bd_sleep:
    bd_sleep.append("Máte dobrý spánek.")

exp_subj = neuron_net_test(sleep_data)

final_report = f"""\n{data_name}
{center_f}
{sleep_data} 
{bd_sleep}

očekávané hodnocení spánku: {exp_subj} hodnocení: {subj_input}

{final_answer}
"""
print(final_report)
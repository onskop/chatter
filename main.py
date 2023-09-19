# First
# streamlit run "c:\Users\oskop\OneDrive - Novavax Inc\Production dev\PyProj\AI\chatter\main.py"
import openai 
import streamlit as st
import tiktoken



def reset_session_state():
    if "init_instructions1" in st.session_state:
        st.session_state['init_instructions1'] = st.session_state['input1']
        instructions1 = st.session_state['init_instructions1']
    if "init_instructions2" in st.session_state:
        st.session_state['init_instructions2'] = st.session_state['input2']
        instructions2 = st.session_state['init_instructions2']

    inicial_msg_state = [
        {"role": "system", "content": instructions1},
        {"role": "system", "content": instructions2},
        {"role": "assistant", "content": "Jsem tvůj výživový poradce. Co tě zajímá?"},
    ]
    st.session_state['messages'] = inicial_msg_state
    st.session_state['conv_price'] = 0


def get_req_price():
    return st.session_state['req_price']

def tokenCheckConv(convo):
  encoding = tiktoken.encoding_for_model(model)
  # concat whole text from messages
  text = ''
  for message in convo:
    text += ' ' + message['content']
  # calculate the price
  return len(encoding.encode(text))

def priceCheckConv(convo, price):
  encoding = tiktoken.encoding_for_model(model)
  # concat whole text from messages
  text = ''
  for message in convo:
    text += ' ' + message['content']
  # calculate the price
  price = price * len(encoding.encode(text))
  return round(price,4)

# -----------------------------------------------------------------------------------------------------------------------------------

# initialize session state -----------------------------------------------------------------------------------------------------------------------------------


if "conv_price" not in st.session_state:
    st.session_state['conv_price'] = 0

if "init_instructions1" not in st.session_state:
    st.session_state['init_instructions1'] = '''Jsi výživový poradce. Odpovídáš na otázky o výživě, stručně a výstižně. K doporučeným receptům přidáš i nákupní seznam a kalorické hodnoty jídel. Při sestavování jídelníčku vezmeš v potaz informace o zdravotním stavu klienta, jeho fyzické parametry jako hmotnost, výška, síla, množství tuku nebo intolerance a alergie. '''
if "init_instructions1" in st.session_state:
    instructions1 = st.session_state['init_instructions1']
    
if "init_instructions2" not in st.session_state:
    st.session_state['init_instructions2'] = "Parametry klienta: Hmotnost: 95kg, Výška: 195cm, Množství tuku: 18%, Intolerance: syrová rajčata, koriandr, kopr"
if "init_instructions2" in st.session_state:
    instructions2 = st.session_state['init_instructions2']


# {"role": "user", "content": "placeholder"}
inicial_msg_state = [
        {"role": "system", "content": instructions1},
        {"role": "system", "content": instructions2},
        {"role": "assistant", "content": "Jsem tvůj výživový poradce. Co tě zajímá?"},
    ]

if "messages" not in st.session_state:
    st.session_state["messages"] = inicial_msg_state

st.write('Změna instrukcí resetne konverzaci.')
col1, col2 = st.columns(2)
with col1:
    st.text_area(label='Styl poradce',value = instructions1, key='input1', height=200, on_change = reset_session_state())
with col2:
    st.text_area(label='Parametry klienta',value = instructions2, key='input2', height=200, on_change = reset_session_state())


openai_api_key = st.secrets["openai_key"]
st.subheader("💬 Chatbot")

for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

# construct form -----------------------------------------------------------------------------------------------------------------------------------

# add 3 text input fields to 3 columns

with st.sidebar:
    st.title("OpenAI Playground")
    model = st.radio('Choose a model', ['gpt-3.5-turbo', 'gpt-4'])
    if model == 'gpt-3.5-turbo':
        price = 0.0000015 # per token
    elif model == 'gpt-4':
        price = 0.00003 # per token
    # make a button to reset session state
    
    if st.button('Reset Session State'):
        reset_session_state()



# main chat -----------------------------------------------------------------------------------------------------------------------------------

if prompt := st.chat_input():

    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model=model, messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)


with st.sidebar:
    st.write('Conversation contains ' + str(tokenCheckConv(st.session_state['messages'])) + ' tokens.') 
    st.write(' Next request price: $' + str(priceCheckConv(st.session_state['messages'], price)))
    st.session_state['conv_price'] += priceCheckConv(st.session_state['messages'], price)
    st.write('Total price: $' + str(round(st.session_state['conv_price'],4)))
    st.subheader('Debug: ')
    st.write(st.session_state.messages)

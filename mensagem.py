from twilio.rest import Client

def smsDoTwilio(codigo:int, tel:str):
    account_sid =  'user_console_twilio'
    auth_token ='token_console_twilio'
    client = Client(account_sid, auth_token)
    client.messages.create(from_="+17seu_numero_twilio", body="Seu código de autenticação é: "+str(codigo), to="+55"+tel) 
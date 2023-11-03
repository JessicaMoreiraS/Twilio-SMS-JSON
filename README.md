# Twilio-SMS-JSON
Envio de SMS utilizando Twilio para confirmação de cadastro com armazenamento dos dados cadastrados em JSON com Tinydb
Programa utliza o console para sua execução utilize as bibliotecas:
```
pip install twilio
```
```
pip install tinydb
```

Execute o programa :
```
pip
```

Funcionamento:
os dados cadastrados são salvos no arquivo <b>Usuarios.json</b>, porém a "validação" fica como "false" até que o usuário insira o código de confirmação enviado em seu telefone via SMS.
Caso o código esteja correto a "validação" será alterada para "true", porém, caso estejá incorreto o usuário será deletado de <b>Usuarios.json</b>, caso queira poderá realizar um novo cadastro.

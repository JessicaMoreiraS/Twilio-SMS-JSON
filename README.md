# Twilio-SMS-JSON
Envio de SMS utilizando Twilio para confirmação de cadastro com armazenamento dos dados cadastrais em JSON com Tinydb
<hr>
<div align="center">
  <img src="https://github.com/JessicaMoreiraS/Twilio-SMS-JSON/assets/100448388/5a79d591-3329-4338-8a8c-aa40911f2f0f" width="50%">
  <br>
  <sub><a href="https://storyset.com/user">User illustrations by Storyset</a></sub>
</div>
<br><br>
<p>Para utilizar esse programa é necessário uma conta na plataforma Twilio: https://www.twilio.com/pt-br</p>
<p>Até a data de criação desse projeto a plataforma permite a criação de conta com créditos gratuitos</p>
<p>Modifique o arquivo <b>connect.py</b> com seu Token, Usuario e telefone (internacional) fornecidos dentro da plataforma Twilio</p>
<p>Utilize as bibliotecas:</p>

```
pip install twilio
```

```
pip install tinydb
```

<p>Execute o programa de <b>main.py</b> :</p>

```
python -u <SEU_DIRETORIO>\Twilio-SMS-JSON\main.py
```

Funcionamento:
<p>os dados cadastrados são salvos no arquivo <b>Usuarios.json</b>, porém a "validação" fica como "false" até que o usuário insira o código de confirmação enviado em seu telefone via SMS.</p>
<p>Caso o código esteja correto a "validação" será alterada para "true", porém, caso estejá incorreto o usuário será deletado de <b>Usuarios.json</b>, caso queira poderá realizar um novo cadastro.</p>
<p>O telefone do cadastro está cadastrado como sendo do Brasil, é necessário informar o DDD</p>
<p>Esse programa é executado dentro do terminal</p>


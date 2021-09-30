#!/usr/bin/python

#######################################################
#Script: 
#Author  :Samantha Reis
#Email   :samanthasreiis@gmail.com
#######################################################


# Importando as bibliotecas 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
import os
import csv
import pandas as pd
from string import Template
from email.header import Header
from email.utils import formataddr
import time

# Função que toma o arquivo com os contatos e tranforma em 
# lista de nome e endereço de email
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[0])
    return names, emails


# Função que cria o corpo do email
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


# Conectando o servidor
server = smtplib.SMTP("smtp.gmail.com", 587,local_hostname="") # caso o servidor for gmail
server.ehlo()
server.starttls()

# Dados de login 
SenderAddress = input('Digite seu email:')
password = input('Digite sua senha:')

# Fazendo o login
server.login(SenderAddress, password)

# Recebendo os dados de email em um arquivo csv e transformando em um txt
csv_file = input('Digite o nome do arquivo em csv: ')

with open('contatos_email.txt', "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()

with open('contatos_email.txt',"r+") as f:
    new_f = f.readlines()
    f.seek(0)
    for line in new_f:
        if "email nome" not in line:
            f.write(line)
    f.truncate()

# lendo os contatos    
emails, names = get_contacts('contatos_email.txt')  

# Criando a mensagem com cada nome da lista de contatos
message_template = read_template('mensagem.txt')

# Mensagem em html 
html =  '''


'''
# carregar anexo imagem

fp = open("images/header.png", 'rb')


# Criando um objeto MIMEImage com o objeto de arquivo acima.
msgImage = MIMEImage(fp.read())


# Não se esqueça de fechar o objeto de arquivo após usá-lo.
fp.close ()


# Adicione o valor do cabeçalho 'Content-ID' ao objeto MIMEImage acima para fazer com que ele se refira à fonte da imagem (src = "cid: image1") no conteúdo Html.
msgImage.add_header('Content-ID', '<image1>')


author = formataddr((str(Header(u'DATA_LABE', 'utf-8')), SenderAddress))

# For em cada contato e enviando o email
for name, email in zip(names, emails):
    msg = MIMEMultipart()       # cria a mensagem
    emailfrom = "Data_Labe"

    # add o nome da pessoa na mensagem base
    message = message_template.substitute(PERSON_NAME= name.title())

    # os parametros da mensagem
    msg['From'] =  author
    msg['To'] = email
    msg['Subject'] = "Novas do Data_ // Estamos de volta!"
    part1 = MIMEText(message, 'plain')
    part2 = MIMEText(html, 'html')


    # Anexe o objeto MIMEImage ao corpo do e-mail.
    msg.attach(msgImage)
    msg.attach(msgImage2)
    msg.attach(msgImage3)
    msg.attach(msgImage4)
    msg.attach(msgImage5)
    msg.attach(msgImage6)
    msg.attach(msgImage7)
    msg.attach(msgImage8)
    msg.attach(msgImage9)
    msg.attach(msgImage10)
    msg.attach(msgImage11)
    msg.attach(msgImage12)





    
    # add a mensagem
    msg.attach(part1)
    msg.attach(part2)



    # enviando a mensagem via servidor
    server.send_message(msg)
    
    del msg
    #time.sleep(1) # Dá uma pausa de 1s entre um email e outro


print('Emails enviados!!')

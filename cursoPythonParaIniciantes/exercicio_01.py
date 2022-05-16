'''
print("-------------------aula 03------------------");
print("Hello world!"); #função para mostrar algo na tela
'''

'''
print("-------------------aula 04------------------");
print('Os Peradores');
print(5+7); #a soma utilisace a sinal de "+"
print(27-6); #a subtração utilisace a sinal de "-"
print(45/5); #a divisão utilisace a sinal de "/"
print(5+8); #a multiplicação utilisace a sinal de "*"
print(2**3); #a exponeciação utilisace a sinal de "**" exe: 2^3
print(31%3); #a resto da divisão utilisace a sinal de "%"
print(14//7); #a pega parteira da divisão utilisace a sinal de "//" OBS: pega só a parte enteira
'''

'''
print("-------------------aula 05------------------");
print('Variaveis numericas');
numero=5; #cria uma variavel chamada "numero" e tribui a ela o valor 5
numero==5; #operador logico que verifica o iqualdade
numero1=6;
resultado=numero+numero1; #riavel resebe a operação
resultado=0; #riavel troca seu valor por 0
print(resultado); #mostra o valor da variavel

print('Tipos Variaveis');
var1=4;
var2=5.3;
word='project schedule';
print(type(var1)); #"type(var1);" função para mostrar a tipo da variavel
print(type(var2)); #"type(var2);" função para mostrar a tipo da variavel
print(type(word)); #"type(word);" função para mostrar a tipo da variavel
'''

'''
print("-------------------aula 06------------------");
print("Função input()");
nome=input("Qual é o seu nome?"); #"input();" faz a leitura de um dado fornecido pelo usuario, depois essa é atribuido esse dado a variavel nome
print("Hello "+nome); #Era fazera concatenação da entring "Hello" mais a variavel "nome"
print("Escreva dois numero para fazer uma conta");
num1=input();
num2=input();
print(num1+num2);
#OBS: o resultado da saida sera errrado pois o tipo de variavel sera erra
#solução possivel para o erro é:
print("Escreva dois numero para fazer uma conta");
num1=int(input()); #a função int(); ira converter a string recebida pelo input im numero int
num2=int(input()); #a função int(); ira converter a string recebida pelo input im numero int
print(num1+num2);
'''

'''
print("-------------------aula 07------------------");
print("Formatações trabalhando variaveis em frases");
fruit="orange"; #cria uma variavel "fruta" e armazena "laranja" nela
print("I would like an %s juice."%fruit); #"%s" era indicara que a variavel "fruit" ira o cupara essa posição
idade=21;
print("I am %d years old."%idade); #"%d" era indicara que a variavel "idade" ira o cupara essa posição
print("My favorite juice is {} juice".format(fruit)); #a função "format();" ira indicar que a variavel "fruit" ira o cupar o locau coma as "{}"
color1='blue';
color2='pink';
print("The sky is {0}. The flower is {1} and my car is {0}.".format(color1,color2)); #comentarios linha debaixo
#a função "format();" ira subistutir os "{}" pelas variaveis as colocando no local correto usando um indixe que começa em zero
conta=17/3;
print('O resultado da conta é: {:.2f}'.format(conta)); #comentarios linha debaixo
# ao se adicionar"{:.2f}" a função passa a expecificar que se dezeja pegar apenas os dois ultimos numeros apos a virgola
'''

print("-------------------aula 08------------------");
print("Condições");
print("Exemplo-01");
food='pizza';
if food=='pizza': #a função "if" ira fazer um teste se for verdadeiro ira izecutar o comando abaixo
    print("Possui muitas calorias");
#-------------------------------------------------------------------------------------------------------------------------
print("Exemplo-02");
food='macarrão'; #subistitui pizza por macarrão
if food=='pizza': #a função "if" ira fazer um teste se for verdadeiro ira izecutar o primerio comando abaixo, se for falso ira executar o segundo comando a baixo
    print("Possui muitas calorias"); #primeiro comando, o primeiro comando começa no primeiro ":" logo a pos o "if"
else:
    print("Desconheço as calorias"); #segundo comando, o segundo comando começa no primeiro ":" logo a pos o "else"
#-------------------------------------------------------------------------------------------------------------------------
print("Exemplo-03");
food='arroz'; #subistitui macarrão por arroz
if food=='pizza': #a função "if" ira fazer um teste se for verdadeiro ira izecutar o primerio comando abaixo, se for falso ira percorre vazendo as verificações ate achar o correto
    print("Possui muitas calorias"); #primeiro comando, o primeiro comando começa no primeiro ":" logo a pos o "if"
elif food=='abobora':
    print('Possui poucas calorias');#segundo comando, o segundo comando começa no primeiro ":" logo a pos o "elif"
elif food=='arroz':
    print('Possui poucas calorias');#terceiro comando, o terceiro comando começa no primeiro ":" logo a pos o segundo "elif", esse mesma logica segui-se cajo haja mais "elif"
    #Obs: no python você pode executar vaios comandos basta que eles obedeção a identação(recuoo de cada linha), veja o exemplo na proxima linha
    print("Aqui é o exemplo de dois codigos");
elif food=='churrasco':
    print("Possui muitas calorias");
elif food=='melão':
    print('Possui poucas calorias');
else: #se nem uma das opções anteriores for verdadeira ira executar o "else"
    print("Desconheço as calorias");
#-------------------------------------------------------------------------------------------------------------------------
print("Exemplo-04");
food='pizza';
if food!='pizza': # a função "if" vai verificar se a comida é diferente de "pizza", se isso for verdadeiro ira executar o primerio comando abaixo, se for falso ira executar o segundo comando a baixo, assim por diante
    # OBS: Ao utilizar "!=" a sentensa vira uma negação então o condição sera a oposta
    print('Não é pizza');
else:
    print("É pizza");
'''
Esse estivesse trabalhando os numeros as condiçôes poderião ser
== testa se inqual
!= testa se é diferente
 > testa se maior
 < testa se menor
>= testa se maior ou igual
<= testa se menor ou igual
'''
#-------------------------------------------------------------------------------------------------------------------------
print("Exemplo-04");
print("Em qual ano você nasseu?");
data=int(input());
ano=2021-data;
if ano>=18:
    print("Você é adulto.");
else:
    print("Você não é adulto");
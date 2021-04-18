import time  # Imports a module to add a pause
import pygame
from sprites import *

# Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]


def quote(sentence):
    print(sentence)
    time.sleep(0.5)

required = ("\nUse only A, B, or C\n")  # Cutting down on duplication


# The story is broken into sections, starting with "intro"
def intro():
    quote("Não se sabe ao certo quando isso começou")
    quote("monstros, guerras, ameaças")
    quote("aquela primeira noite foi o momento mais triste da humanidade")
    quote("várias almas perdidas, corações e laços rompidos")
    time.sleep(2)
    quote("Filha, você ainda é muito nova para tudo isso")
    quote("não posso exigir muito de você")
    quote("espero que tenha uma boa vida com seu pai")
    quote("quando eu voltar, vai ser no dia em que tudo estará acabado")
    time.sleep(2)
    quote("- Finalmente, a idade mínima")
    quote("- Hora de sair dessa espelunca, não vejo a hora de te ver denovo mamãe.")
    time.sleep(2)
    quote("P - Filha")
    quote("T - Oi?")
    quote("P - Imaginei que você dissesse isso... infelizmente não posso te deixar continuar.")
    quote("T - Pai, já conversamos sobre isso... eu treinei minha infância toda pra esse momento, ninguém nessa ilha é mais capacitada do que eu!")
    quote("P - Eu imagino filha, mas a Ilha Victória não é um lugar pra brincadeiras, como eu poderia viver todos os dias com você correndo esse perigo!?")
    quote("T - Pai, por favor... a mamãe foi pra lá pela primeira vez com apenas 12 anos!! ainda nem existia o exame de admissão naquela época, e mesmo assim ela voltou sã e salva.")
    quote("P - Ai ai... não tem como te convencer né? uma certa parte de mim quer que você descubra esse mundo por sí só... apenas me prometa uma coisa, Tawna.")
    quote("T - O que, pai? qualquer coisa para agradar o senhor!!")
    quote("P - Quando você ver que as coisas estão ruins, volte o mais rápido possível pra casa, ok?")
    quote("T - tudo bem, Pai. Vou apenas trazer a mamãe de volta rapidinho, relaxe!")
    quote("P - hahaha, se apenas fosse tão fácil... mas tudo bem, uma promessa entre nós.")
    quote("T - Adeus, pai. Até logo...")
    time.sleep(2)
    quote("")
    quote("")
    quote("")
    quote("TAWNA E O CÉU ESCARLATE")
    quote("Prólogo")
    quote("")
    quote("")
    quote("")
    quote("S - Haha! olha só quem vem aí, se não é a aspirante a nova aventureira da cidade.")
    quote("T - ...")
    quote("S - Você realmente acha que com esse corpo mole consegue vencer aquele exame impossivel?")
    quote("T - Sinto muito, sarah, mas não dá de conversar agora...")
    quote("S - kkkkkk, se você não tem coragem nem de me enfrentar, como acha que vai vencer as provações?")
    quote("T - E o que você quer que eu faça? fique que nem você, uma covarde?")
    quote("S - Hmpf... você e aquela garota de cabelos enrolados, sempre se achando as rainhas do mundo.")
    quote("S - Como se tudo fosse possível na base da vontade.")
    quote("S - Se eu, uma atleta e lutadora nata, já falhei por 3 vezes seguidas, você acha que com 16 aninhos e um coração alegre será o suficiente? mesmo sendo esperta e ágil, você é muito novinha ainda.")
    quote("T - Olha... eu realmente desejo muito encontrar minha mãe, mesmo que eu tenha que enfrentar coisas surreais")
    quote("T - Sinto que a cada segundo que perco, a situaçao dela pode piorar.")
    quote("S - Você só irá se matar...")
    quote("T - Haha! você tem é medo de uma menina mais jovem que você ser capaz de vencer a prova...")
    quote("T - Se não me engano, a tal menina dos cabelos enrolados é mais nova que você também...")
    quote("T - Esse seu orgulho frágil apenas mostra sua incapacidade de vencer a prova...")
    quote("S - ...Pois bem então, estava tentando lhe incentivar a desistir apenas com palavras, mas tô vendo que não dá certo.")
    quote("S - ...então terei que resolver isso na base da força. Não me culpe se quebrar seu corpo hahahah")
    quote("T - Sempre na base do soco, você sempre foi assim.")
    quote("S - Que seja! você vai me agradecer depois, pois estou salvando sua vida te impedindo de ir àquela ilha amaldiçoada.")
    quote("T - Vem pra cima então!")


#intro()
fight(Tawna, Sarah)
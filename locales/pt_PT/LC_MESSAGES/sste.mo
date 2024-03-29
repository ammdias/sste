��    W      �     �      �  �  �     h     t     �     �     �     �     �     �     �  %   �     �            	        '     -     <  ?   U  C   �     �     �     �     �     �     �           
            $      +      2      9   �  >      �"     �"  )   �"     %#  
   3#  �  >#    %(  5   )/     _/     y/  
   �/     �/     �/     �/     �/     �/     �/     �/     �/     0     0  
   0      0     90  
   E0     P0     \0     l0     y0  	   �0     �0     �0  
   �0     �0     �0     �0     �0     �0     �0     �0     �0     �0     �0     �0     1     1  	   1     !1     .1     J1     d1     1    �1    �2     �M     �M     �M     �M     �M     �M     �M     N     N  ,   N     BN     ON     ]N     fN     wN     ~N  $   �N  Q   �N  d   O     kO     rO     yO     �O     �O     �O     �O     �O     �O     �O     �O     �O     �O  �  �O     �R     �R  +   �R     �R     �R  �  �R  4  �X  L   �_  "   	`     ,`     >`     U`     m`     �`     �`     �`     �`     �`     �`     �`     �`     a      a     6a     Ga     Ta     ba     ya  !   �a     �a     �a     �a  	   �a     �a  	   �a     �a     �a     �a     �a  	   b     b     b     b     *b     3b  	   Fb  	   Pb     Zb  !   kb     �b     �b     �b     0              M       L                   E       =               >       6          
   :   4            <   /   D          ?   S       (   I   G               .                    9          5       '   2   H              F       7       )       ,      8   #       %       $               "   @   -       R   Q   ;          &   C   U   W           *   +          K   O      A      1   	          J   3          V   P                     T                    !      B   N    
Secure Simple Text Editor

Copyright (C) 2019 António Manuel Dias
contact: ammdias@gmail.com

This program comes with ABSOLUTELY NO WARRANTY;  for details use command
'sste.py --warranty' or go to 'Help > Warranty' on the graphical user
interface.

This is free software, and you are welcome to redistribute it under certain
conditions; use command 'sste.py --copyright' or go to 'Help > Copyright' on
the graphical user interface for details.

----

SSTE is a text editor (simple text) that stores the files encrypted
by GnuPG, either with a symmetric encryption key or [several] public keys.

Encryption with public keys allows the sharing of an encrypted text document
by a group of people without the need to share a common password, encrypting the
document with the public keys of all people who needs access it. Encryption with
public keys is also convenient for a single user, as it doesn't require a
password input at saving the documents, only for opening.

Encryption with symmetric keys, the default, must be used when at least one of
the users doesn't have a GnuPG private/public key pair.

Depends on Python 3.4+, with Tkinter, and GnuPG 2.


Installation and first run
==========================

To install, simply uncompress the zip file, navigate to the uncompressed
directory and run 'sste.py' with Python 3.

Alternately, in Linux or other Unix-like operating system, you may use the
included installation script to install the program:

    $ python3 INSTALL.py

The program will try to find the GnuPG executable in the PATH.  If it can not
find it, it will prompt the user to manually provide the path in the Settings
Dialog (see below).  If GnuPG is not installed in your system, please download
it from the system's software store or, at your option, from the GnuPG site:

* https://gnupg.org/download/index.html


Usage
=====

The program works as any common graphical simple-text editor.  You may insert,
delete, select, copy and paste text as usual.  When saving, you will be prompted
to insert and confirm a password to encrypt the file.  Similarly, when opening
a file the program will ask for a password to decrypt the file.  If public keys
are used to encrypt the file, the password to the keys will only be asked when
opening the file.

Below is a description of the menu items and its actions:

File menu
---------

* New: start editing a new file.  If the file you were currently editing was
       modified since the last save you will be prompted to save it.

* Open: open a saved file.  When prompted insert the password used to encrypt
        the file or to open the private key to decrypt it.

* Save: save the current file. If you are using symmetric encryption, which is
        the default, enter the secret password to encrypt the file when
        prompted.

* Save as: save the current file with a different name.

* Save to: save the current file encrypted for a selected list of GnuPG
           recipients (using its public keys). Select all the intended
           recipients in the list and press 'Ok'. Only recipients in the
           default keyring and with valid public keys are shown.  Be sure to
           always select your public, in addition to the keys of all other
           recipients that need to access the file. If you forget to add your
           public key, you won't be able to open the file yourself, as
           only the users with the private keys corresponding to the chosen
           public keys can decrypt the file.

* Quit: close the program.  You will be prompted to save the file if it has
        changed since the last save.

Edit menu
---------

* Undo: undo most recent change in the text.

* Redo: redo most recent undo in the text.

* Cut: cut the selected text into the clipboard.

* Copy: copy the selected text to the clipboard.

* Paste: insert the clipboard text.

* Find: find pieces of text in the editor.  Insert the text to find in the
        dialog and press 'ENTER'.  If the text is found it will be selected and
        shown in the editor window.  If not found, a warning will be given
        that the end of the file was reached -- you may restart the search
        from the top of the file.  Press 'ESCAPE' to close the dialog.

* Replace: replace pieces of text in the editor.  Insert the text to find and
           the text to replace it in the dialog and press 'ENTER'.  If the
           text is found, you will be asked if you want to replace it.

* Select all: select all text in the editor.

* Settings: change the settings of the editor. Available options:

    * Text color: change the color of the text. Click the button to open the
            color choosing dialog.
    * Background color: change the background (paper) color.  Click the button
            to open the color choosing dialog.
    * GnuPG path: choose the correct path to the GnuPG executable.  Click the
            button to open the file dialog.
    * GnuPG default recipients. Click the button to open the recipients dialog.
            The default recipients (may be just one) are the public keys that
            will be used to encrypt all the files at saving time, except if
            using the 'Save To' option. Be sure to always select your public
            key, or you won't be able to open the file -- only the users with
            the corresponding private keys to the chosen public keys can decrypt
            the file.

Help menu
---------

* Manual: display this dialog.

* About: display information about the program.

* Copyright: display the copyright information.

* Warranty: display the warranty information.


Uninstall application
=====================

The program may be uninstalled from the terminal with the command:

    $ sste --uninstall

or, from within the folder where the program is installed:

    $ python3 UNINSTALL.py
 <Control-S> <Control-a> <Control-f> <Control-n> <Control-o> <Control-q> <Control-r> <Control-s> <F1> At least one recipient must be given. Background color Background color: Cancel Clear All Close Close document Could not execute GnuPG. Could not find GnuPG in the PATH.
Please configure it manually. Could not load '.config' file.
Starting with default configuration. Ctrl+A Ctrl+C Ctrl+F Ctrl+N Ctrl+O Ctrl+Q Ctrl+S Ctrl+Shift+S Ctrl+Shift+Z Ctrl+V Ctrl+X Ctrl+Z Cu_t Editor for secure (encrypted) simple text files
(C) 2019 António Manuel Dias

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>. Error F1 File has changed. Do you want to save it? File:  {}  {} Find text: From the GNU General Public License:
    
15. Disclaimer of Warranty.

THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE
COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS"
WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING,
BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY
AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE PROGRAM PROVE
DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR
CORRECTION.

16. Limitation of Liability.

IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR
CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES
ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT
NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES
SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO
OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY
HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
 From the Preamble of the GNU General Public License:
        
The GNU General Public License is a free, copyleft license for
software and other kinds of works.

The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

See the file 'gpl.txt' on the program's directory for more details.
If it's missing please refer to http://www.gnu.org/licenses/gpl.txt
 GnuPG command, including complete path if not on PATH GnuPG default recipients: GnuPG error:
{} GnuPG path GnuPG path: Go to top of document? Ok Re_do Replace current selection? Replace text Replace with: Save _As... Save _To... Search Select All Select GnuPG recipients: Select _All Text color Text color: Text not found. [ Modified ] [ New secure text file ] [ Saved ] _About _Copy _Copyright _Edit _File _Find... _Help _Manual _New _Open... _Paste _Quit _Replace... _Save _Settings... _Undo _Warranty file to open show copyright information. show version information. show warranty information. uninstall application Project-Id-Version: 1.2
PO-Revision-Date: 2023-12-09 20:20+WET
Last-Translator: António Manuel Dias <ammdias@gmail.com>
Language-Team: pt_PT <ammdias>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: UTF-8
Generated-By: pygettext.py 1.5
 
Secure Simple Text Editor

Copyright (C) 2019 António Manuel Dias
contacto: ammdias@gmail.com

Este programa é distribuído SEM QUALQUER GARANTIA;  para mais detalhes use o
comando 'sste.py --warranty' ou use 'Ajuda > Garantia' na interface
gráfica.

Este programa é software livre e pode ser redistribuído sob determinadas
condições;  use o comando 'sste.py --copyright' ou use 'Ajuda > Licença'
na interface gráfica para mais detalhes.

----

SSTE é um editor de texto (texto simples) que guarda os ficheiros cifrados
pelo GnuPG, usando uma chave simétrica ou chaves públicas.

Cifrar com chaves públicas permite a partilha de um documento de texto entre
um grupo de pessoas sem a necessidade de partilhar uma senha comum, cifrando
o documento com as chaves públicas de todas as pessoas que necessitam de lhe
aceder. Cifrar com chave pública é igualmente conveniente para um único
utilizador, já que não requere a inserção de uma senha ao gaurdar
documentos, apenas para os abrir.

Deve cifrar-se com uma chave simétrica, a opção configurada por omissão,
quando pelo menos um dos utilizadores não possuir um par de chaves GnuPG
pública/privada.
Depende de Python 3.4+, com Tkinter, e GnuPG 2.

Instalação e primeira execução
==============================

Para instalar basta descomprimir o ficheiro zip, entrar na diretoria criada
e correr o programa 'sste.py' com o Python 3.

Em alternativa, em Linux ou outros sistemas derivados de Unix, pode usar
o script de instalação incluído para instalar o programa:

    $ python3 INSTALL.py

O programa tentará encontrar o executável do GnuPG no PATH.  Não o
conseguindo, pedirá ao utilizador para providenciar a sua localização
manualmente no Diálogo de Configuração (ver abaixo).  Se não tiver o GnuPG
instalado no seu sistema, por favor instale-o a partir da loja de software
do sistema ou, se desejar, a partir do site do GnuPG:

* https://gnupg.org/download/index.html


Utilização
==========

O programa funciona como qualquer editor gráfico de texto simples.  Pode
inserir, apagar, selecionar, copiar e colar texto como habitualmente. Ao
guardar ser-lhe-á pedida uma senha e sua confirmação para cifrar o ficheiro.
De igual forma, ao abrir um ficheiro o programa pedirá uma senha para o
decifrar.  Se forem usadas chaves públicas para cifrar o ficheiro, a senha
para usar as chaves será pedida apenas ao abrir o ficheiro.

Em baixo pode encontrar uma descrição dos itens de menu e suas ações:

Menu Ficheiro
-------------

* Novo: iniciar a edição de um novo ficheiro.  Se o ficheiro que se
        encontrava a editar tiver sido alterado após a última vez que foi
        guardado, ser-lhe-á perguntado se o deseja guardar.

* Abrir: abrir um ficheiro guardado.  Quando pedido, insira a senha usada
         para cifrar o ficheiro ou para abrir a chave privada para o
         decifrar.

* Guardar: guardar o ficheiro atual.  Se estiver a usar cifra simétrica, o
           que é a opção configurada por omissão, insira a senha secreta para
           cifrar o ficheiro.

* Guardar como: guardar o ficheiro atual com um nome diferente.

* Guardar para: guardar o ficheiro atual cifrado para uma lista de destinatários
                GnuPG selecionada (usando as suas chaves públicas). Selecione
                todos os destinatários pretendidos na lista e pressione 'Ok'.
                Apenas os destinatários com chaves públicas válidas no chaveiro
                GnuPG serão mostradas.  Assegure-se que inclui sempre a sua
                própria chave pública, em conjunto com as de todos os outros
                destinatários que necessitam de acesso ao finheiro. Se se
                esquecer de selecionar a sua chave pública, não poderá abrir
                o ficheiro, já que apenas os utilizadores detendo as chaves
                privadas correspondentes às públicas usadas para cifrar o
                ficheiro o poderão decifrar.

* Sair: fechar o programa.  Ser-lhe-á perguntado se deseja guardar o ficheiro
        se este tiver sido alterado desde a última vez que foi guardado.

Menu Editar
-----------

* Desfazer: desfazer a alteração mais recente.

* Refazer: refazer a última alteração desfeita.

* Cortar: cortar o texto selecionado para a área de transferência.

* Copiar: copiar o texto selecionado para a área de transferência.

* Colar: inserir o texto da área de transferência.

* Procurar: procurar pedaços de texto no editor.  Inserir o texto a procurar
            no diálogo e pressionar 'ENTER'.  Se o texto for encontrado, será
            selecionado e mostrado na janela do editor.  Em caso contrário,
            será mostrado um aviso de que chegou ao fim do ficheiro -- pode
            reiniciar a procura a partir do início.  Pressione 'ESCAPE' para
            fechar o diálogo.

* Substituir: substituir partes do texto no editor.  Insera o texto a procurar
              e o texto para o substituir no diálogo e pressione 'ENTER'.  Se
              o texto for encontrado, ser-lhe-á perguntado se o deseja
              substituir.

* Selecionar tudo: selecionar todo o texto no editor.

* Configuração: alterar a configuração do editor.  Ao terminar, pressione
                'ENTER' para ativar as alterações ou 'ESCAPE' para as reverter.
                Opções disponíveis:

    * Cor do texto: alterar a cor do texto.  Clicar no botão para abrir o
                    diálogo de escolha de cor.
    * Cor do fundo: alterar a cor do fundo.  Clicar no botão para abrir o
                    diálogo de escolha de cor.
    * Localização do GnuPG: escolher a localização correta do executável do
                    GnuPG.  Clicar no botão para abrir o diálogo de escolha do
                    ficheiro.
    * Destinatários GnuPG configurados: clique o botão para abrir o diálogo
                de escolha de destinatários. Os destinatários configurados
                (pode ser apenas um) são as chaves públicas que serão usadas
                para cifrar todos os ficheiros sempre que forem guardados,
                excepto quando usada a opção 'Guardar Para'. Assegure-se que
                inclui a sua chave pública ou não poderá abrir o ficheiro --
                apenas os utilizadores com chaves privadas correspondentes
                às chaves públicas escolhidas podem decifrar o ficheiro.

Menu Ajuda
----------

* Manual: mostrar este diálogo.

* Sobre: mostrar informação sobre o programa.

* Licença: mostrar a licença de utilização do programa.

* Garantia: mostrar informação sobre a garantia do programa.


Desinstalar aplicação
=====================

O programa pode ser desinstalado a partir do terminal com o comando:

    $ sste --uninstall

ou, a partir da pasta onde o programa está instalado:

    $ python3 UNINSTALL.py
 <Control-S> <Control-a> <Control-f> <Control-n> <Control-o> <Control-q> <Control-r> <Control-s> <F1> Tem de fornecer pelo menos um destinatário. Cor do fundo Cor do fundo: Cancelar Limpar Seleção Fechar Fechar documento Não foi possível executar o GnuPG. Não foi possível encontrar o GnuPG no PATH.
Por favor, configure-o manualmente. Não foi possível ler o ficheiro '.config'.
Iniciando o programa com a configuração por omissão. Ctrl+A Ctrl+C Ctrl+F Ctrl+N Ctrl+O Ctrl+Q Ctrl+S Ctrl+Shift+S Ctrl+Shift+Z Ctrl+V Ctrl+X Ctrl+Z Cort_ar Editor de ficheiros de texto simples seguros (cifrados)
(C) 2019 António Manuel Dias

Este programa é software livre: pode redistribui-lo e/ou modificá-lo
sob os termos da Licença Pública Geral GNU, tal como publicada pela
Free Software Foundation, quer a versão 3 da Licença ou, se desejar,
qualquer versão mais recente.

Este programa é distribuído na esperança de ser útil, mas SEM QUALQUER
GARANTIA; sem mesmo a garantia implícita de COMERCIALIZAÇÃO ou
UTILIDADE PARA QUALQUER FIM ESPECÍFICO.  Consulte a Licença Pública
Geral GNU para mais informação.

Deve ter recebido uma cópia da Licença Pública Geral GNU em conjunto
com este programa.  Se não, consulte <https://www.gnu.org/licenses/>. Erro F1 O ficheiro foi alterado. Deseja guardá-lo? Ficheiro:  {}  {} Texto a procurar: Da Licença Pública Geral GNU:

15. Exclusão de Garantia.

NÃO HÁ QUALQUER GARANTIA PARA O PROGRAMA, NO LIMITE PERMITIDO PELA LEI
APLICÁVEL.  EXCEPTO QUANDO DE OUTRA FORMA ESTABELECIDO POR ESCRITO, OS
TITULARES DOS DIREITOS DE AUTOR E/OU OUTRAS PARTES, FORNECEM O PROGRAMA
"COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, TANTO EXPRESSA COMO
IMPLÍCITA, INCLUINDO, ENTRE OUTRAS, AS GARANTIAS IMPLÍCITAS DE
COMERCIABILIDADE E ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA. O RISCO QUANTO
À QUALIDADE E DESEMPENHO DO PROGRAMA É SEU. CASO O PROGRAMA CONTENHA
DEFEITOS, O UTILIZADOR ARCARÁ COM OS CUSTOS DE TODOS OS SERVIÇOS,
REPARAÇÕES OU CORREÇÕES NECESSÁRIAS.

16. Limites de Responsabilidade.

EM NENHUMA CIRCUNSTÂNCIA, A MENOS QUE EXIGIDO PELA LEI APLICÁVEL OU SEJA
ACORDADO POR ESCRITO, QUALQUER TITULAR DE DIREITOS DE AUTOR OU QUALQUER
OUTRA PARTE QUE ALTERE E/OU FORNEÇA O PROGRAMA CONFORME PERMITIDO ACIMA,
SERÁ RESPONSÁVEL PELOS DANOS DO UTILZIADOR, INCLUINDO ENTRE OUTROS,
QUAISQUER DANOS GERAIS, ESPECIAIS, FORTUITOS OU EMERGENTES, RESULTANTES
DO USO OU IMPOSSIBILIDADE DE USO DO PROGRAMA (INCLUINDO, ENTRE OUTROS,
PERDAS DE DADOS OU DADOS GERADOS DE FORMA IMPRECISA, PERDAS SOFRIDAS
PELO UTILIZADOR OU TERCEIROS OU A IMPOSSIBILIDADE DO PROGRAMA DE OPERAR
COM QUAISQUER OUTROS PROGRAMAS), MESMO QUE ESSE TITULAR OU OUTRA PARTE,
TENHA SIDO ALERTADA SOBRE A POSSIBILIDADE DE OCORRÊNCIA DESSES DANOS.
 Do Preâmbulo da Licença Pública Geral GNU:
        
A Licença Pública Geral GNU é uma licença livre para software e outros
tipos de trabalhos.

As licenças da maioria do software e outros trabalhos práticos são
elaboradas de forma a suprimir a liberdade de os partilhar e modificar.
Pelo contrário, a Licença Pública Geral GNU visa garantir a liberdade
de partilhar e modificar todas as versões de um programa para assegurar
que o software permaneça livre para todos os seus utilizadores.  Nós, na
Free Software Foundation, usamos a Licença Pública Geral GNU para a maioria
do nosso software; também se aplica a qualquer outra obra distribuída desta
forma pelos seus autores.  Pode aplicá-la igualmente aos seus programas.

Quando falamos de software livre referimo-nos à liberdade, não ao preço.
As nossas Licenças Públicas Gerais visam garantir-lhe a liberdade de
distribuir cópias de software livre (e cobrar por isso se desejar), que
receba o código-fonte ou o possa obter se desejar, que o possa modificar
ou usar partes dele em novos programas livres; e que esteja ciente de que
o pode fazer.

Para proteger os seus direitos necessitamos de evitar que alguém lhos negue
ou solicite que lhes renuncie.  Assim, tem determinadas responsabilidades
no caso de distribuir cópias do software ou se o modificar.

Por exemplo, se distribuir cópias de um programa assim licenciado, seja
gratuitamente ou mediante pagamento, terá de conceder aos receptores os
direitos que possui.  Terá de garantir que, também eles, recebam ou possam
obter o código-fonte.  E terá a obrigação de lhes mostrar estes termos,
para que conheçam os seus direitos.

Consulte o ficheiro 'gpl.txt' na directoria do programa para mais detalhes.
Se não o encontrar, por favor consulte a licença em
http://www.gnu.org/licenses/gpl.txt
 Comando do GnuPG, incluindo a localização completa se não estiver no PATH Destinatários GnuPG configurados: Erro no GnuPG:
{} Localização do GnuPG Localização do GnuPG: Ir para o início do documento? Ok _Refazer Substituir o texto selecionado? Substituir texto Substituir por: Guardar _Como... Guardar _Para... Procurar Selecionar Tudo Selecionar destinatários GnuPG: Selecionar _Tudo Cor do texto Cor do texto: Texto não encontrado. [ Modificado ] [ Novo ficheiro de texto seguro ] [ Guardado ] _Sobre _Copiar _Licença _Editar _Ficheiro _Procurar... _Ajuda _Manual _Novo _Abrir... Co_lar Sai_r _Substituir... _Guardar C_onfiguração... _Desfazer _Garantia ficheiro a abrir mostrar licença de utilização. mostrar versão da aplicação. mostrar garantia. desinstalar aplicação 
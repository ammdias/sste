��    N      �  k   �      �  �  �     t     �     �     �     �     �     �     �     �     �     �     �            C   $     h     }     �     �     �     �     �     �     �     �     �     �     �     �     �  �  �     �     �     �     �  )   �  
     �      �  5   �&     4'  
   D'     O'     ['  	   r'     |'     �'     �'     �'     �'     �'  
   �'     �'     �'     �'     (     (  
   (     (     %(     +(     4(     :(     B(     G(     P(     W(     ](     i(     o(     |(  	   �(     �(     �(     �(     �(    �(  �  �)     �:     �:     �:     �:     �:     ;     ;     ;     );     .;     ;;     I;     P;  $   _;  d   �;  $   �;  &   <     5<     <<     C<     J<     Q<     X<     _<     f<     s<     �<     �<     �<     �<  �  �<  #   n?     �?     �?     �?  +   �?     �?  �  �?  4  iE  L   �L     �L     �L     M     ,M     LM     SM     \M     |M     �M     �M     �M     �M     �M     �M     �M     �M     N  	   N     N  	    N     *N     7N     >N     FN  	   LN     VN     ]N     cN     rN     {N  	   �N  	   �N     �N  !   �N     �N     �N     H      9   ?   $                   J   >       .       )           "   6       @                  L       !       M   2   *   G                 	   3      <       ;   '       7   8   #       B           K      1                     +             &       E          F   /   4      D   I   C   (                   5      ,   
      0      A                   -          %      =      :         N    
Secure Simple Text Editor

Copyright (C) 2021 António Manuel Dias
contact: ammdias@gmail.com

This program comes with ABSOLUTELY NO WARRANTY;  for details use command
'sste.py --warranty' or go to 'Help > Warranty' on the graphical user
interface.

This is free software, and you are welcome to redistribute it under certain
conditions; use command 'sste.py --copyright' or go to 'Help > Copyright' on
the graphical user interface for details.

----

SSTE is a simple-text editor that stores the files encrypted by GnuPG with its
default symmetric algorithm.  It depends on GnuPG and Python 3 with Tkinter.


Installation and first run
==========================

To install, simply uncompress the zip file, navigate to the uncompressed
directory and run 'sste.py' with Python 3.

Alternately, in Linux or other Unix-like operating system, you may use the
included installation script to install the program for a single user:

    $ bash local_install.sh

The program will try to find the GnuPG executable in the PATH.  If it can not
find it, it will prompt the user to manually provide the path in the Settings
Dialog (see below).  If GnuPG is not installed in your system, please download
it from the system's software store or, at your option, from the GnuPG site:

* https://gnupg.org/download/index.html


Usage
=====

The program works as any common graphical simple-text editor.  You may insert,
delete, select, copy and paste text as usual.  When saving you will be prompted
to insert and confirm a password to encrypt the file.  Similarly, when opening
a file the program will ask for a password to decrypt the file.

Below is a description of the menu items and its actions:

File menu
---------

* New: start editing a new file.  If the file you were currently editing was
       modified since the last save you will be prompted to save it.

* Open: open a saved file.  When prompted insert the password used to encrypt
        the file and press 'ENTER'.  Press 'ESCAPE' to stay editing the same
        file.

* Save: save the current file.  Insert the password to encrypt the file,
        confirm it and then press 'ENTER' to save the file.  Press 'ESCAPE'
        to cancel.

* Save as: save the current file with a different name.

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

* Settings: change the settings of the editor.  When finished, press 'ENTER'
            to activate changes and close the dialog or 'ESCAPE' to reset the
            changes.  Available options:

    * Text color: change the color of the text. Click the button to open the
                  color choosing dialog.
    * Background color: change the background (paper) color.  Click the button
                        to open the color choosing dialog.
    * GnuPG path: choose the correct path to the GnuPG executable.  Click the
                  button to open the file dialog.

Help menu
---------

* Manual: display this dialog.

* About: display information about the program.

* Copyright: display the copyright information.

* Warranty: display the warranty information.
 <Control-S> <Control-a> <Control-f> <Control-n> <Control-o> <Control-q> <Control-r> <Control-s> <F1> Background color Background color: Close Confirm: Could not execute GnuPG. Could not load '.config' file.
Starting with default configuration. Could not open file. Could not write to file. Ctrl+A Ctrl+C Ctrl+F Ctrl+N Ctrl+O Ctrl+Q Ctrl+S Ctrl+Shift+S Ctrl+Shift+Z Ctrl+V Ctrl+X Ctrl+Z Cu_t Editor for secure (encrypted) simple text files
(C) 2021 António Manuel Dias

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>. Entered passwords don't match. Error Error: F1 File has changed. Do you want to save it? Find text: From the GNU General Public License:
    
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
 GnuPG command, including complete path if not on PATH GnuPG error:
{} GnuPG path GnuPG path: Go to top of document? Password: Re_do Replace current selection? Replace text Replace with: Save _As... Select _All Text color Text color: Text not found. Wrong password. _About _Copy _Copyright _Edit _File _Find... _Help _Manual _New _Open... _Paste _Quit _Replace... _Save _Settings... _Undo _Warranty file to open show copyright information. show version information. show warranty information. Project-Id-Version: 0.2
PO-Revision-Date: 2021-02-28 14:20+WET
Last-Translator: Antńio Manuel Dias <ammdias@gmail.com>
Language-Team: pt_PT <ammdias>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: UTF-8
Generated-By: pygettext.py 1.5
 
Secure Simple Text Editor

Copyright (C) 2021 António Manuel Dias
contact: ammdias@gmail.com

Este programa é distribuído SEM QUALQUER GARANTIA;  para mais detalhes use o
comando 'sste.py --warranty' ou use 'Ajuda > Garantia' na interface
gráfica.

Este programa é software livre e pode ser redistribuído sob determinadas
condições;  use o comando 'sste.py --copyright' ou use 'Ajuda > Licença'
na interface gráfica para mais detalhes.

----

O SSTE é editor de texto simples que cifra os ficheiros com o algoritmo de
cifra simétrica padrão do GnuPG. Necessita do GnuPG e Python 3 com Tkinter.


Instalação e primeira execução
==============================

Para instalar basta descomprimir o ficheiro zip, entrar na diretoria criada
e correr o programa 'sste.py' com o Python 3.

Alternativamente, em Linux ou outros sistemas derivados de Unix, pode usar
o script de instalação incluído para instalar o programa para um único
utilizador:

    $ bash local_install.sh

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
decifrar.

Em baixo pode encontrar uma descrição dos itens de menu e suas ações:

Menu Ficheiro
-------------

* Novo: iniciar a edição de um novo ficheiro.  Se o ficheiro que se
        encontrava a editar tiver sido alterado após a última vez que foi
        guardado, ser-lhe-á perguntado se o deseja guardar.

* Abrir: abrir um ficheiro guardado.  Insira a senha quando lhe for pedido e
         pressione 'ENTER'.  Pressione 'ESCAPE' se desejar continuar a editar
         o ficheiro atual.

* Guardar: guardar o ficheiro atual.  Insira a senha para cifrar o ficheiro,
           confirme na caixa abaixo e pressione 'ENTER'.  Pressione 'ESCAPE'
           para cancelar.

* Guardar como: guardar o ficheiro atual com um nome diferente.

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

* Selecionar tudo: selecionar todo o texto no editor.

* Configuração: alterar a configuração do editor.  Ao terminar, pressione
                'ENTER' para ativar as alterações ou 'ESCAPE' para as reverter.
                Opções disponíveis:

    * Cor do texto: alterar a cor do texto.  Clicar no botão para abrir o
                    diálogo de escolha de cor.
    * Cor do fundo: alterar a cor do fundo.  Clicar no botão para abrir o
                    diálogo de escolha de cor.
    * Localização do GnuPG: escolher a localização correta do executável do
                            GnuPG.  Clicar no botão para abrir o diálogo de
                            escolha do ficheiro.

Menu Ajuda
----------

* Manual: mostrar este diálogo.

* Sobre: mostrar informação sobre o programa.

* Licença: mostrar a licença de utilização do programa.

* Garantia: mostrar informação sobre a garantia do programa.
 <Control-S> <Control-a> <Control-f> <Control-n> <Control-o> <Control-q> <Control-r> <Control-s> <F1> Cor do fundo Cor do fundo: Fechar Confirmação: Não foi possível executar o GnuPG. Não foi possível ler o ficheiro '.config'.
Iniciando o programa com a configuração por omissão. Não foi possível abrir o ficheiro. Não foi possível guardar o ficheiro. Ctrl+A Ctrl+C Ctrl+F Ctrl+N Ctrl+O Ctrl+Q Ctrl+S Ctrl+Shift+S Ctrl+Shift+Z Ctrl+V Ctrl+X Ctrl+Z Cort_ar Editor de ficheiros de texto simples seguros (cifrados)
(C) 2021 António Manuel Dias

Este programa é software livre: pode redistribui-lo e/ou modificá-lo
sob os termos da Licença Pública Geral GNU, tal como publicada pela
Free Software Foundation, quer a versão 3 da Licença ou, se desejar,
qualquer versão mais recente.

Este programa é distribuído na esperança de ser útil, mas SEM QUALQUER
GARANTIA; sem mesmo a garantia implícita de COMERCIALIZAÇÃO ou
UTILIDADE PARA QUALQUER FIM ESPECÍFICO.  Consulte a Licença Pública
Geral GNU para mais informação.

Deve ter recebido uma cópia da Licença Pública Geral GNU em conjunto
com este programa.  Se não, consulte <https://www.gnu.org/licenses/>. Senhas introduzidas não coincidem. Erro Erro: F1 O ficheiro foi alterado. Deseja guardá-lo? Texto a procurar: Da Licença Pública Geral GNU:

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
 Comando do GnuPG, incluindo a localização completa se não estiver no PATH Erro no GnuPG:
{} Localização do GnuPG Localização do GnuPG: Ir para o início do documento? Senha: _Refazer Substituir o texto selecionado? Substituir texto Substituir por: Guardar _Como... Selecionar _Tudo Cor do texto Cor do texto: Texto não encontrado. Senha errada. _Sobre _Copiar _Licença _Editar _Ficheiro _Procurar... _Ajuda _Manual _Novo _Abrir... Co_lar Sai_r _Substituir... _Guardar C_onfiguração... _Desfazer _Garantia ficheiro a abrir mostrar licença de utilização. mostrar versão da aplicação. mostrar garantia. 
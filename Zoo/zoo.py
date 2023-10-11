print("I love animals! \n"
      "Let's check out the animals...\n"
      "The deer looks fine.\n"
      "The lion looks healthy.")
camel = r"""
 ___.-''''-.
/___ @      |
',,,,.      |         _.'''''''._
      '     |        /            \
      |     \    _.-'              \
      |      '.-'                   '-.
      |                                ',
      |                                  '',
      ',,-,                              ':;
           ',,| ;,,                    ,' ;;
              ! ; !'',,,',',,,,'!     ;   ;:
             : ;  ! !       ! ! ;   ;     :;
            ; ;    ! !      ! !   ; ;     ;,
           ; ;     ! !     ! !    ; ;
          ; ;      ! !     ! !    ; ;
         ;,,        !,!    !,!    ;,;
         /_I        L_I    L_I    /_I
Look at that!"""

lion = r"""
The lion habitat...
                                                      ,w.
                                                   ,YWMMw ,M ,
                              _.---.._   __..---._.'MMMMMw,wMWmW,
                        _.-""        '''            YP"WMMMMMMMMMb,
                    .-'__.'                      .'     MMMMW^WMMMM;
        _,        .'.-'"; `,        /`      .--""       :MMM[==MWMW^;
     ,mM^"      ,-'.'  /    ;      ;       /    ,         MMMMb_wMW" @\
    ,MM:.     .'.-'   .'      ;     `\    ;      `,        MMMMMMMW `"=./`-,
    WMMm__,-'.'       /       _.\      F'''-+,,    ;_,_. dMMMMMMMM[,_ / `=_}
    "^MP__.-'      ,-' _.--""    `-,  ;        \    ; ;MMMMMMMMMMW^``; __|
                  / .'              ; ;          )   )`{  \ `"^W^`,    \ :
                 / .'              /   (        .'  /     Ww._   `. `"
                / Y,               `,   `-,=,_{    ;      MMMP`""-, `-._.-,
                (--, )                `,_ / `) \/"")       ^"     `-, -;"\:
The lion is roaring!"""

deer = r"""
The deer habitat...
   /|       |\
`__\\        //__'
   ||       ||
 \__`\      |'__/
   `_\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;`-'   `---__________-----.-.
     ;;;                         \_\
     ';;;                         |
      ;    |                      ;
       \    \    \      |        /
        \_,  \   /       \      |\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/            /_/   /_/
Pretty good!"""

goose = r"""
The goose habitat...

                                     _
                                 ,-"" "".
                               ,' ____   `.
                             ,' ,'    `.   `._
   (`.          _..--.._   ,' ,'        \     \
  (`-.\    .-""         ""' /           (  d _b
 (`._  `-"" ,._            (             `-(   \
<_    `    ( <`<            \               `-._\
 <`-        (__< <          :          
  (__        (_<_<          ;
   `------------------------------------------
Beautiful!"""

bat = r"""
The bat habitat...
_________________             _________________
 ~-.             \  |\___/|  /              .-~
      ~-.         \ / o o \ /            .-~
         >         \\  W  //            <
        /           /~---~               \
       /_          |      |              _\
         ~-.       |                  .-~
            ;       \     /          i
           /___     /\   /\      ___\
               ~-. /  \_/  \ .-~
                  V         V
It's doing fine."""

rabbit = r"""
The rabbit habitat...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /    "~" |
  Y      _, |
 /|  ;-"~ _ l
/ l/ ,-"~   \
\//\/     .- \
 Y       /    Y
 l       I    !
 ]\      _\   /"\
(" ~----( ~  Y.  )
 It looks fine!"""


animals = [camel, lion, deer, goose, bat, rabbit]

while True:
    try:
        selected_animals = int(input())
        if -7 < selected_animals < 6:
            print(animals[selected_animals])

        elif selected_animals == 200:
            break

        else:
            print("please enter a number from -6 to 5 or 200 to exit")

    except ValueError:
        print("please enter a number from -6 to 5 or 200 to exit")
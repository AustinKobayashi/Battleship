import time

class Animator:

    #def __init__(self):


    def attack_animation(self):
        frame0 = '''     /\         __/___ 
     ||   _____/______|           
  ___/\__/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame1 = '''     /\\
     ||
     /\         __/___ 
     **   _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame2 = '''     /\\
     ||
     /\\
     **         __/___ 
     **   _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame3 = '''     /\\
     ||
     /\\
     **
     **         __/___ 
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame4 = '''     /\\
     ||
     /\\
     **
     **
                __/___ 
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame5 = '''     /\\
     ||
     /\\
     **
     **
     
                __/___ 
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame6 = '''     /\\
     ||
     /\\
     **
     **
     
     
                __/___ 
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame7 = '''     /\\
     ||
     /\\
     **
     **
     
     
     
                __/___ 
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print(frame0)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame1)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame2)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame3)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame4)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame5)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame6)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame7)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        self.flying_animation()


    def flying_animation(self):

        frame0 = '''  /\       
 /  \ 
 |  | 
 |  |
/ == \\
|/**\|
  **\n'''

        frame1 = '''  /\       
 /  \ 
 |  | 
 |  |
/ == \\
|/**\|
  **
  **'''

        frame2 = '''  /\       
 /  \ 
 |  | 
 |  |
/ == \\
|/**\|
  **
  *'''

        frame3 = '''  /\       
 /  \ 
 |  | 
 |  |
/ == \\
|/**\|
  **\n'''

        frame4 = '''  /\       
 /  \ 
 |  | 
 |  |
/ == \\
|/**\|
  **
   *'''

        frame5 = '''  /\       
 /  \ 
 |  | 
 |  |
/ == \\
|/**\|
  **
  **'''

        for i in range(3):
            print(frame0)
            time.sleep(0.1)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

            print(frame1)
            time.sleep(0.1)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

            print(frame2)
            time.sleep(0.1)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

            print(frame3)
            time.sleep(0.1)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

            print(frame4)
            time.sleep(0.1)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

            print(frame5)
            time.sleep(0.1)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')



    def hit_animation(self):
        frame0 = '''               **
               **
               \/
               ||
               \/

     
     
     
                __/___ 
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame1 = '''               **
               **
               \/
               ||
               \/ 
     
     
                __/___ 
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame2 = '''               **
               **
               \/
               ||
               \/ 
     
                __/___ 
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame3 = '''               **
               **
               \/
               || 
               \/
                __/___ 
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame4 = '''             '.\|/.'
             (\   /)
             - -O- -
             (/   \)
             ,'/|\\'.__ 
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame5 = '''         '.  \ | /  ,'
           `. `.' ,'
          ( .`.|,' .)
          - ~ -0- ~ -_ 
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame6 = '''          . ','|` ` .
           .'  "  '
         ,   ' , '  `_ 
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame7 = '''             (  ) (
              ) ( )
              (  )
               ) /____
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame8 = '''              ) ( )
              (  )
               ) (
               ) /____
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame9 = '''              (  ) (
               ) (
               ( )
               ) /____
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame10 = '''              ( ) (
               ( )
               ) (
               ) /____
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print(frame0)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame1)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame2)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame3)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame4)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame5)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame6)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame7)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame8)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame9)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame10)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')



    def miss_animation(self):

        frame0 = '''               **
               **
               \/
               ||
               \/


  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame1 = '''               **
               **
               \/
               ||
               \/ 


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame2 = '''               **
               **
               \/
               ||
               \/  

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame3 = '''               **
               **
               \/
               || 
               \/  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame4 = '''            \ \  /  / 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame5 = '''        \  \ \  |  / /  /
            \ \  /  / 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame6 = '''      \  \  \ \ | /  / /  /
        \  \ \  | / /  /
          \ \ \  /  / /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame7 = '''        \  \ \  |  / /  /
            \ \  /  / 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame8 = '''            \ \  /  / 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame9 = '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print(frame0)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame1)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame2)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame3)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame4)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame5)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame6)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame7)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame8)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame9)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


    def sink_animation(self):

        frame0 = '''             (  ) (
              ) ( )
              (  )
               ) /____
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame1 = '''             (  ) (
              ) ( )
              (  )
               ) /____
          _____/______|           
  _______/_____\_______\_____        
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame2 = '''             (  ) (
              ) ( )
              (  )
               ) /____
          _____/______|                   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame3 = '''             (  ) (
              ) ( )
              (  )
               ) /____                
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame4 = '''             (  ) (
              ) ( )
              (  )              
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame5 = '''             (  ) (
              ) ( )          
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame6 = '''             (  ) (        
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        frame7 = '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print(frame0)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame1)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame2)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame3)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame4)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame5)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame6)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(frame7)
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')






















# U-Tuber
Multiple Number of youtube videos and playlist downloader just by one click .


For Python2.x 

        To start the app for first time  
        
              chmod +x python2_setup.sh
              ./python2_setup.sh


For Python3.x 

        To start the app for first time  
        
              chmod +x python3_setup.sh
              ./python3_setup.sh


Then Run this -

chmod +x path_setup.sh

./path_setup.sh



Now you can open U-Tuber from any directory any time by just using -

For Python2.x  $utuber2 
For Python2.x  $utuber3 




Manually installing requirements :-

   python2.7

   Tkinter : 
   
             pip install python-tk
   
             sudo apt-get install python-tk
               
   
   
   pytube :
   
   
             pip install pytube
             
             
             or Download .tar.gz file and install
             


Run :-
      
      python u_Download.py



python3.x
   Python3.x:
            sudo apt-get install python3 
            
            sudo apt-get install python3-pip 

   Tkinter : 
   
             pip install python3-tk
   
             sudo apt-get install python3-tk
               
   
   
   pytube :
   
   
             pip3 install pytube
             
             
             or Download .tar.gz file and install
             


Run :-
      
      python3 u_Download_python3.py




    
If running behind proxy add following lines in code

pip install urllib2 

         import urllib2
         proxy = urllib2.ProxyHandler({'http':'<username>:<password>@<proxy>:<port>', 'https':'<username>:<password>@<proxy>:<port>'})
         opener = urllib2.build_opener(proxy)
         urllib2.install_opener(opener)

Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\Harshana B\Desktop\Experiments\5. cannibals.py


	Game Start
Now the task is to move all of them to right side of the river
rules:
1. The boat can carry at most two people
2. If cannibals num greater than missionaries then the cannibals would eat the missionaries
3. The boat cannot cross the river by itself with no people on board

M M M C C C |	 --- | 

Left side -> right side river travel
Enter number of Missionaries travel => 1
Enter number of Cannibals travel => 1


M M C C | --> | M C 

Right side -> Left side river travel
Enter number of Missionaries travel => 1
Enter number of Cannibals travel => 0


M M M C C | <-- | C 

Left side -> right side river travel
Enter number of Missionaries travel => 0
Enter number of Cannibals travel => 2


M M M | --> | C C C 

Right side -> Left side river travel
Enter number of Missionaries travel => 0
Enter number of Cannibals travel => 1


M M M C | <-- | C C 

Left side -> right side river travel
Enter number of Missionaries travel => 2
Enter number of Cannibals travel => 0


M C | --> | M M C C 

Right side -> Left side river travel
Enter number of Missionaries travel => 1
Enter number of Cannibals travel => 1


M M C C | <-- | M C 

Left side -> right side river travel
Enter number of Missionaries travel => 2
Enter number of Cannibals travel => 0


C C | --> | M M M C 

Right side -> Left side river travel
Enter number of Missionaries travel => 0
Enter number of Cannibals travel => 1


C C C | <-- | M M M 

Left side -> right side river travel
Enter number of Missionaries travel => 0
Enter number of Cannibals travel => 2


C | --> | M M M C C 

Right side -> Left side river travel
Enter number of Missionaries travel => 1
Enter number of Cannibals travel => 0


M C | <-- | M M C C 

Left side -> right side river travel
Enter number of Missionaries travel => 1
Enter number of Cannibals travel => 1


| --> | M M M C C C 

You won the game : 
	Congrats
Total attempt
11

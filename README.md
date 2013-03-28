![Blackbox](https://raw.github.com/DarrenMowat/blackbox-sb2/master/doc/Blackbox.png)

Blackbox is a Haskell source code transformer which allows you to find out interesting things about your program. The main aim of Blackbox is to act as a backend for text editor plugins which helps to expose the type system of Haskell to the user.

This is a plugin developed using Blackbox for Sublime Text 2. The plugin currently supports 
  * Splitting Pattern Variables
  * Listing variables in scope & their types at a given point in a program
  * Inserting missing type lines for functions
 
 ## Installation

1. Download & Install the Blackbox binary from: https://github.com/DarrenMowat/blackbox 
2. Download & Install Sublime Text 2 from: http://www.sublimetext.com/
3. Install Sublime Package Control, the plugin manager for Sublime Text 2, from: http://wbond.net/sublime_packages/package_control/installation
4.  Open the SB2 command menu by pressing Ctrl-Shift-P on Linux or Cmd-Shift-P on Mac. Navigate to ‘Package Control: Add Repository’ and hit enter. Enter ‘https://github.com/DarrenMowat/blackbox-sb2' as the repository to add. 
5. Open the SB2 command menu and select to ‘Package Control: Install Package’. Next select ‘blackbox-sb’ to install the plugin. 

In some cases the Blackbox plugin will be unable to find the path of the ghci or blackbox binaries. If this is the case a few further installation steps are required 

1. Go to Preferences > Package Settings > Blackbox > Settings - User
2. Add the following to that file and set the paths for ghci & blackbox. You can get these paths by calling `which ghci` & `which blackbox`

    {
	    "ghci_path": "",
	    "blackbox_path": ""
    }
 
3. You may have to restart Sublime Text 2 for the settings to be loaded.  

## Usage 

### Splitting Pattern Variables

Highlight the variables on the left hand side of the binding as shown below:

![Pre Split](https://raw.github.com/DarrenMowat/blackbox-sb2/master/doc/dsplitpre.png)

Open the SB2 command menu (Ctrl-Shift-P on Linux or Cmd-Shift-P on Mac) and navigate to ‘Blackbox: Split Highlighted Pattern Variables’. The patterns will then be split by Blackbox.

![Post Split](https://raw.github.com/DarrenMowat/blackbox-sb2/master/doc/dsplitpost.png)



### Listing whats in Scope

Highlight the right hand side of the binding that you want to find the scope for:

![Pre Scope](https://raw.github.com/DarrenMowat/blackbox-sb2/master/doc/scopepre.png)

Open the SB2 command menu (Ctrl-Shift-P on Linux or Cmd-Shift-P on Mac) and navigate to ‘Blackbox: What Variables are in Scope’. A comment containing a list of variables and their types will be inserted by Blackbox.

![Post Scope](https://raw.github.com/DarrenMowat/blackbox-sb2/master/doc/scopepost.png)

### Inserting function types

Highlight the name of the function you want the type to be inserted for.

![Pre Insert](https://raw.github.com/DarrenMowat/blackbox-sb2/master/doc/idpre.png)

Open the SB2 command menu (Ctrl-Shift-P on Linux or Cmd-Shift-P on Mac) and navigate to ‘Blackbox: Insert Type Line for Function’. The type line for the function will then be inserted at the start of the function declaration.

![Post Insert](https://raw.github.com/DarrenMowat/blackbox-sb2/master/doc/idpost.png)



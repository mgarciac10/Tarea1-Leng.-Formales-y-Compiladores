from automata.fa.dfa import DFA

dfa = DFA(
    states={"0", "1", "2"},
    input_symbols={"0", "1"},
    transitions={
        "0": {"0": "0", "1": "1"},
        "1": {"0": "2", "1": "0"},
        "2": {"0": "1", "1": "2"},
    },
    initial_state="0",
    final_states={"0"},
)

def CheckString(string):
    if dfa.accepts_input(string):
        print("The DFA accepts the string '" + string + "'")
    else:
        print("The DFA rejects the string '" + string + "'")

if __name__ == "__main__":

    print('\033[93m' + "Para salir del programa, ingrese 'exit' o 'salir' en la cadena a evaluar" + '\033[0m')

    while True:
        string = input("Ingrese la cadena a evaluar: ")
        if string == "exit" or string == "salir":
            break
        CheckString(string)
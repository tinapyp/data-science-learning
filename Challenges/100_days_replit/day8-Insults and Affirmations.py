print(
    """
Productive Machine
""",
    end="\n",
)
name = input("ur Name > ")
print(f"Hi {name}, happy to see you here")
question = input("what u whanna to know? ")
if question.lower() == "aplikasi" or question.lower() == "tutorial":
    print(
        f"""
Just Download notion {name}, then learn it from youtube u will knowing it better that me i think, or u can just go into my youtube @tinApyp and learn there

Hope this help u {name}
With love from me 😘
  """
    )
    last = input("any more question? (y/N) ")
    if last == "y":
        _ = input("???? stil doenst know? ")
        print(" GO Search bruhhh hahahhaha")
    elif last == "n":
        print(f"great, {name}. come again if any question")
    else:
        print("FOLLOW THE INSTRUCTION")
else:
    print("tutorial or aplikasi?")


a = """mutation($recipient: String!, $amount: Int!) { 
  transfer(recipient: $recipient, amount: $amount) { 
    money 
  } 
}"""

print(a)
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "06e7dc31-2688-44b9-b735-76b403d2a746",
   "metadata": {},
   "outputs": [],
   "source": [
    "def shift_letter(letter, shift):\n",
    "    '''Shift Letter.\n",
    "    5 points.\n",
    "\n",
    "    Shift a letter right by the given number.\n",
    "    Wrap the letter around if it reaches the end of the alphabet.\n",
    "\n",
    "    Examples:\n",
    "    shift_letter(\"A\", 0) -> \"A\"\n",
    "    shift_letter(\"A\", 2) -> \"C\"\n",
    "    shift_letter(\"Z\", 1) -> \"A\"\n",
    "    shift_letter(\"X\", 5) -> \"C\"\n",
    "    shift_letter(\" \", _) -> \" \"\n",
    "\n",
    "    *Note: the single underscore `_` is used to acknowledge the presence\n",
    "        of a value without caring about its contents.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    letter: str\n",
    "        a single uppercase English letter, or a space.\n",
    "    shift: int\n",
    "        the number by which to shift the letter.\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    str\n",
    "        the letter, shifted appropriately, if a letter.\n",
    "        a single space if the original letter was a space.\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    Alphabet =\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"\n",
    "  \n",
    "    for i in range(len(Alphabet)):\n",
    "        if Alphabet[i] == letter:\n",
    "            Output = (i + shift)%26\n",
    "            \n",
    "    if letter == \" \":\n",
    "        return \" \"\n",
    "        \n",
    "    return Alphabet[Output]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "cb1b8b9c-a6aa-403a-9971-02c1ab887078",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C'"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "shift_letter(\"X\",5) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "9c135144-cc58-4f41-abdd-f2bcc9cfc2a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def caesar_cipher(message, shift):\n",
    "    '''Caesar Cipher.\n",
    "    10 points.\n",
    "\n",
    "    Apply a shift number to a string of uppercase English letters and spaces.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    message: str\n",
    "        a string of uppercase English letters and spaces.\n",
    "    shift: int\n",
    "        the number by which to shift the letters.\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    str\n",
    "        the message, shifted appropriately.\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    Alphabet = \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"\n",
    "    new_message=\"\"# \n",
    "    for x in range(len(message)):\n",
    "        for i in range(len(Alphabet)):\n",
    "            if message[x] == Alphabet[i]:\n",
    "                Output = (i + shift)%26\n",
    "                for letter in message:\n",
    "                    new_message = new_message+Alphabet[Output]\n",
    "                    break\n",
    "        \n",
    "    return new_message\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "fe7a3ce3-da94-49c0-b48a-3c7f47cb8550",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'RFWYD'"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "caesar_cipher(\"MARTY\", 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "0a1e61b0-b93f-4c14-bd38-f0fa23b41eef",
   "metadata": {},
   "outputs": [],
   "source": [
    "def shift_by_letter(letter, letter_shift):\n",
    "    '''Shift By Letter.\n",
    "    10 points.\n",
    "\n",
    "    Shift a letter to the right using the number equivalent of another letter.\n",
    "    The shift letter is any letter from A to Z, where A represents 0, B represents 1,\n",
    "        ..., Z represents 25.\n",
    "\n",
    "    Examples:\n",
    "    shift_by_letter(\"A\", \"A\") -> \"A\"\n",
    "    shift_by_letter(\"A\", \"C\") -> \"C\"\n",
    "    shift_by_letter(\"B\", \"K\") -> \"L\"\n",
    "    shift_by_letter(\" \", _) -> \" \"\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    letter: str\n",
    "        a single uppercase English letter, or a space.\n",
    "    letter_shift: str\n",
    "        a single uppercase English letter.\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    str\n",
    "        the letter, shifted appropriately.\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    Alphabet =\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"\n",
    "    \n",
    "    letter_position = None\n",
    "    shift_position = None\n",
    "    for i in range(len(Alphabet)):\n",
    "        if Alphabet[i]==letter_shift:\n",
    "            shift_position = i\n",
    "    for x in range(len(Alphabet)):\n",
    "        if Alphabet[x]==letter:\n",
    "            letter_position=x\n",
    "    \n",
    "    Output = (letter_position + shift_position)%26\n",
    "    \n",
    "    return Alphabet[Output]\n",
    "    \n",
    "          "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "98d695d4-3ae8-4ae6-921b-33cf8c789219",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'J'"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "shift_by_letter(\"Z\", \"K\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "017b3f81-1866-4180-a401-71a0daf45340",
   "metadata": {},
   "outputs": [],
   "source": [
    "def vigenere_cipher (message, key):\n",
    "    '''Vigenere Cipher.\n",
    "    15 points.\n",
    "\n",
    "    Encrypts a message using a keyphrase instead of a static number.\n",
    "    Every letter in the message is shifted by the number represented by the\n",
    "        respective letter in the key.\n",
    "    Spaces should be ignored.\n",
    "\n",
    "    Example:\n",
    "    vigenere_cipher(\"A C\", \"KEY\") -> \"K A\"\n",
    "\n",
    "    If needed, the keyphrase is extended to match the length of the key.\n",
    "        If the key is \"KEY\" and the message is \"LONGTEXT\",\n",
    "        the key will be extended to be \"KEYKEYKE\".\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    message: str\n",
    "        a string of uppercase English letters and spaces.\n",
    "    key: str\n",
    "        a string of uppercase English letters. Will never be longer than the message.\n",
    "        Will never contain spaces.\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    str\n",
    "        the message, shifted appropriately.\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    alphabet = \"abcdefghijklmnopqrstuvwxyz\"\n",
    "    shifted_message = \"\"\n",
    "    for i, char in enumerate(message):\n",
    "        if char in alphabet:\n",
    "            char_index = alphabet.index(char)\n",
    "            shifted_char = key[i % len(key)]\n",
    "            shifted_char_index = alphabet.index(shifted_char)\n",
    "            new_index = (char_index + shifted_char_index) % len(alphabet)\n",
    "            shifted_message += alphabet[new_index]\n",
    "        else:\n",
    "            shifted_message += char\n",
    "\n",
    "    return shifted_message\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "29920aba-b1e1-4c20-b0ad-0e6a0d495018",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'keykey'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vigenere_cipher(\"aaaaaa\", \"key\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "cf8643dd-ac9a-4db0-b46c-96e8a7b80029",
   "metadata": {},
   "outputs": [],
   "source": [
    "def scytale_cipher(message, shift):\n",
    "    '''Scytale Cipher.\n",
    "    15 points.\n",
    "\n",
    "    Encrypts a message by simulating a scytale cipher.\n",
    "\n",
    "    A scytale is a cylinder around which you can wrap a long strip of\n",
    "        parchment that contained a string of apparent gibberish. The parchment,\n",
    "        when read using the scytale, would reveal a message due to every nth\n",
    "        letter now appearing next to each other, revealing a proper message.\n",
    "    This encryption method is obsolete and should never be used to encrypt\n",
    "        data in production settings.\n",
    "\n",
    "    You may read more about the method here:\n",
    "        https://en.wikipedia.org/wiki/Scytale\n",
    "\n",
    "    You may follow this algorithm to implement a scytale-style cipher:\n",
    "    1. Take a message to be encoded and a \"shift\" number.\n",
    "        For this example, we will use \"INFORMATION_AGE\" as\n",
    "        the message and 3 as the shift.\n",
    "    2. Check if the length of the message is a multiple of\n",
    "        the shift. If it is not, add additional underscores\n",
    "        to the end of the message until it is.\n",
    "        In this example, \"INFORMATION_AGE\" is already a multiple of 3,\n",
    "        so we will leave it alone.\n",
    "    3. This is the tricky part. Construct the encoded message.\n",
    "        For each index i in the encoded message, use the character at the index\n",
    "        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.\n",
    "        If this number doesn't make sense, you can play around with the cipher at\n",
    "         https://dencode.com/en/cipher/scytale to try to understand it.\n",
    "    4. Return the encoded message. In this case,\n",
    "        the output should be \"IMNNA_FTAOIGROE\".\n",
    "\n",
    "    Example:\n",
    "    scytale_cipher(\"INFORMATION_AGE\", 3) -> \"IMNNA_FTAOIGROE\"\n",
    "    scytale_cipher(\"INFORMATION_AGE\", 4) -> \"IRIANMOGFANEOT__\"\n",
    "    scytale_cipher(\"ALGORITHMS_ARE_IMPORTANT\", 8) -> \"AOTSRIOALRH_EMRNGIMA_PTT\"\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    message: str\n",
    "        a string of uppercase English letters and underscores (underscores represent spaces)\n",
    "    shift: int\n",
    "        a positive int that does not exceed the length of message\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    str\n",
    "        the encoded message\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    if len(message) % shift != 0:\n",
    "        message += \"_\" * (shift - (len(message) % shift))\n",
    "    \n",
    "    decoded_message = \"\"\n",
    "    for i in range(len(message)):\n",
    "        \n",
    "        position = (i // shift) + (len(message) // shift) * (i % shift)\n",
    "        decoded_message += message[position]\n",
    "    \n",
    "    \n",
    "    return decoded_message"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "8883e437-424a-4f14-bcd4-b5b32b464521",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'IMNNA_FTAOIGROE'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scytale_cipher(\"INFORMATION_AGE\", 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "cb767b14-25b4-4cba-9286-6a227624835c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def scytale_decipher(message, shift):\n",
    "    '''Scytale De-cipher.\n",
    "    15 points.\n",
    "\n",
    "    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.\n",
    "\n",
    "    Example:\n",
    "    scytale_decipher(\"IMNNA_FTAOIGROE\", 3) -> \"INFORMATION_AGE\"\n",
    "    scytale_decipher(\"AOTSRIOALRH_EMRNGIMA_PTT\", 8) -> \"ALGORITHMS_ARE_IMPORTANT\"\n",
    "    scytale_decipher(\"IRIANMOGFANEOT__\", 4) -> \"INFORMATION_AGE_\"\n",
    "\n",
    "    There is no further brief for this number.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    message: str\n",
    "        a string of uppercase English letters and underscores (underscores represent spaces)\n",
    "    shift: int\n",
    "        a positive int that does not exceed the length of message\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    str\n",
    "        the decoded message\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    if len(message) % shift != 0:\n",
    "        message += \"_\" * (shift - (len(message) % shift))\n",
    "    \n",
    "    decrypted_message = \"\"\n",
    "    for i in range(len(message)):\n",
    "        \n",
    "        position = (i // (len(message) // shift)) + (i % (len(message) // shift)) * shift\n",
    "        decrypted_message += message[position]\n",
    "    \n",
    "    \n",
    "    return decrypted_message"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "1d480f63-5dc1-4e9d-8111-aed1d8a55e89",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'INFORMARION_AGE'"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scytale_decipher(\"IMNNA_FRAOIGROE\", 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da404009-9be3-42cb-8123-1931db7828dc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

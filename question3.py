{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question 3\n",
    "\n",
    "#Question:\n",
    "#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.\n",
    "#Suppose the following input is supplied to the program:\n",
    "#8\n",
    "#Then, the output should be:\n",
    "#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}\n",
    "\n",
    "#Hints:\n",
    "#In case of input data being supplied to the question, it should be assumed to be a console input.\n",
    "#Consider use dict()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "please enter a number8\n",
      "{1: 1}\n",
      "{2: 4}\n",
      "{3: 9}\n",
      "{4: 16}\n",
      "{5: 25}\n",
      "{6: 36}\n",
      "{7: 49}\n",
      "{8: 64}\n"
     ]
    }
   ],
   "source": [
    "# = int(input('please enter a number'))\n",
    "# = int(x)\n",
    "#for x in range(1,n +1):\n",
    "#   d = {x : x * x}\n",
    "#   print(d) \n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number:8\n",
      "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}\n"
     ]
    }
   ],
   "source": [
    "#n=int(input(\"Enter a number:\"))\n",
    "#d={x:x*x for x in range(1,n+1)}\n",
    "#print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question:6\n",
    "#Write a program that calculates and prints the value according to the given formula:\n",
    "#Q = Square root of [(2 * C * D)/H]\n",
    "#Following are the fixed values of C and H:\n",
    "#C is 50. H is 30.\n",
    "#D is the variable whose values should be input to your program in a comma-separated sequence.\n",
    "#Example\n",
    "#Let us assume the following comma separated input sequence is given to the program:\n",
    "#100,150,180\n",
    "#The output of the program should be:\n",
    "#18,22,24\n",
    "\n",
    "#Hints:\n",
    "#If the output received is in decimal form, it should be rounded off to its nearest value \n",
    "#(for example, if the output received is 26.0, it should be printed as 26)\n",
    "#In case of input data being supplied to the question, it should be assumed to be a console input. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100,150,180\n",
      "18,22,24\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "c=50\n",
    "h=30\n",
    "value = []\n",
    "items=[x for x in input('please enter numbers: ').split(',')]\n",
    "for d in items:\n",
    "    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))\n",
    "print (','.join(value))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
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

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question 4\n",
    "\n",
    "\n",
    "#Question:\n",
    "#Write a program which accepts a sequence of comma-separated numbers from console and generate a list\n",
    "#and a tuple which contains every number.\n",
    "#Suppose the following input is supplied to the program:\n",
    "#34,67,55,33,12,98\n",
    "#Then, the output should be:\n",
    "#['34', '67', '55', '33', '12', '98']\n",
    "#('34', '67', '55', '33', '12', '98')\n",
    "\n",
    "#Hints:\n",
    "#In case of input data being supplied to the question, it should be assumed to be a console input.\n",
    "#tuple() method can convert list to tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please add some numbers seperated by commas: 34,67,55,33,12,98\n",
      "['34', '67', '55', '33', '12', '98']\n",
      "('34', '67', '55', '33', '12', '98')\n"
     ]
    }
   ],
   "source": [
    "values = input(\"Please add some numbers seperated by commas: \")\n",
    "l = values.split(\",\")\n",
    "t = tuple(l)\n",
    "print(l)\n",
    "print(t)"
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

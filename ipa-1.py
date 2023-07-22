{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "36e91154-98e5-481f-9dfd-7f351f5dc28c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def savings(gross_pay, tax_rate, expenses):\n",
    "    '''Savings.\n",
    "    5 points.\n",
    "\n",
    "    This function calculates the money remaining\n",
    "        for an employee after taxes and expenses.\n",
    "\n",
    "    To get the take-home pay of an employee, we will\n",
    "        follow the following process:\n",
    "        1. Apply the tax rate to the gross pay of the employee; round down\n",
    "        2. Subtract the expenses from the after-tax pay of the employee\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    gross_pay: int\n",
    "        the gross pay of an employee for a certain time period, expressed in centavos\n",
    "    tax_rate: float\n",
    "        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)\n",
    "    expenses: int\n",
    "        the expenses of an employee for a certain time period, expressed in centavos\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the number of centavos remaining from an employee's pay after taxes and expenses\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    float(tax_rate)\n",
    "    take_home_pay = gross_pay - (gross_pay*tax_rate)-expenses\n",
    "    return int(take_home_pay)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4415fbc0-0553-4ecb-9387-f149d3483736",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3500"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "savings (5000, 0.1, 1000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "a31df8cf-ca84-4a3c-b068-fcabf34206c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def material_waste(total_material, material_units, num_jobs, job_consumption):\n",
    "    '''Material Waste.\n",
    "    5 points.\n",
    "\n",
    "    This function calculates how much material input will be wasted\n",
    "        after running a certain number of jobs that consume\n",
    "        a set amount of material.\n",
    "\n",
    "    To get the waste of a set of jobs:\n",
    "        1. Multiply the number of jobs by the material consumption per job.\n",
    "        2. Subtract the total material consumed from the total material available.\n",
    "\n",
    "    The users of this function also want you to format the output as a string, annotated with the\n",
    "        units in which the material is expressed. Do not add a space between the number and the unit.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    total_material: int\n",
    "        the total material available\n",
    "    material_units: str\n",
    "        the units used to express a quantity of the material (e.g., \"kg\", \"L\", etc.)\n",
    "    num_jobs: int\n",
    "        the number of jobs to run\n",
    "    job_consumption: int\n",
    "        the amount of material consumed per job\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    str\n",
    "        the amount of remaining material expressed with its unit (e.g., \"10kg\").\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    str(material_units)\n",
    "    waste = int(total_material - (num_jobs*job_consumption))\n",
    "    result = str(waste) + \" \"+ material_units\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "415b9a8b-d252-4c73-9314-4139895063e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'494 kg'"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "material_waste(500, \"kg\", 2, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "8c3e6ded-02d8-4cec-a488-adc718537863",
   "metadata": {},
   "outputs": [],
   "source": [
    "def interest(principal, rate, periods):\n",
    "    '''Interest.\n",
    "    5 points.\n",
    "\n",
    "    This function calculates the final value of an investment after\n",
    "        gaining simple interest over a number of periods.\n",
    "\n",
    "    To calculate simple interest, simply multiply the principal to the quantity (rate * time).\n",
    "        Add this amount to the principal to get the final value.\n",
    "\n",
    "    Round down the final amount.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    principal: int\n",
    "        the principal (i.e., starting) amount invested, expressed in centavos\n",
    "    rate: float\n",
    "        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)\n",
    "    periods: int\n",
    "        the number of periods invested\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the final value of the investment\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    float(rate)\n",
    "    result = principal + ((rate*principal)*periods)\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "fbd84e8c-5075-4871-97cd-eb5feed43eca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "190.0"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "interest (100, 0.3, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "069a18a3-2ac5-4528-8c48-0aabe7b4bcf5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def body_mass_index(weight, height):\n",
    "    '''Body Mass Index.\n",
    "    5 points.\n",
    "\n",
    "    This function calculates the body mass index (BMI) of a person\n",
    "        given their weight and height.\n",
    "\n",
    "    The formula for BMI is: kg / (m ^ 2)\n",
    "        (i.e., kilograms over meters squared)\n",
    "\n",
    "    Unfortunately, the users of this function use the imperial system.\n",
    "        You will need to first convert their arguments to the metric system.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    weight: float\n",
    "        the weight of the person, in pounds\n",
    "    height: list\n",
    "        the height of the person, expressed as a list of two integers.\n",
    "        the first integer is the foot component of their height.\n",
    "        the second integer is the inches component of their height.\n",
    "        for example, 5'10\" would be passed as [5, 10].\n",
    "\n",
    "    We have not yet discussed lists, but use the skills you developed\n",
    "        in the command line exercise. How would you learn how to work with\n",
    "        lists?\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    float\n",
    "        the BMI of the person.\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    float(weight)\n",
    "    kg_weight=weight*0.453592\n",
    "    meter_height=((list[0]*12)+list[1])*0.0254\n",
    "    BMI = kg_weight/(meter_height**2)\n",
    "    return float(BMI)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "f670a301-8d56-4c9e-af08-7fafd5007d05",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20.372086174067647"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "body_mass_index(130.073, [5,7])"
   ]
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

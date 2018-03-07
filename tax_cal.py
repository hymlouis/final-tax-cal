
# coding: utf-8

# In[63]:
successful_case=0
total_case=0

#MPF contributions. 5% of salary, capped at $15,000
#Married person's allowance
married_allowance = 264000

#Basic allowance
basic_allow = 132000

#Net chargeable income calculator
def MPF_calculator (yrsalary):
        MPF = (yrsalary) * 0.05
        if MPF < 15000:
            return MPF
        else:
            MPF = 15000
            return MPF

def net_char_income_calculator(yrsalary):
    net_char_income = yrsalary - MPF_calculator(yrsalary) - basic_allow
    return net_char_income

def tax_thereon(yrsalary):
        nci=net_char_income_calculator(yrsalary)
        tax_thereon=0
        if nci<45000:
            tax_thereon=nci*0.02
            return tax_thereon
        elif nci<90000:
            tax_thereon=900+(nci-45000)*0.07
            return tax_thereon
        elif nci<135000:
            tax_thereon=900+3150+(nci-90000)*0.12
            return tax_thereon
        elif nci>=135000:
            tax_thereon=900+3150+5400+(nci-135000)*0.17
            return tax_thereon
    
def tax_payable (yrsalary):
        tax_t=tax_thereon(yrsalary)
        tax_deduction=0
        if tax_t*0.75>20000:
            tax_deduction=20000
        else: 
            tax_deduction=tax_t*0.75
        tax=tax_t-tax_deduction
        if tax<0:
            tax=0
        return tax

def joint_tax (hyrsalary,wyrsalary):
        hnci=net_char_income_calculator(hyrsalary)
        wnci=net_char_income_calculator(wyrsalary)
        joint_net_income=hnci+wnci
        if joint_net_income<45000:
            joint_tax_thereon=joint_net_income*0.02
        elif joint_net_income<90000:
            joint_tax_thereon=900+(joint_net_income-45000)*0.07
        elif joint_net_income<135000:
            joint_tax_thereon=900+3150+(joint_net_income-90000)*0.12
        elif joint_net_income>=135000:
            joint_tax_thereon=900+3150+5400+(joint_net_income-135000)*0.17
        if joint_tax_thereon*0.75>20000:
            tax_deduction=20000
        else: 
            tax_deduction=joint_tax_thereon*0.75
        tax=joint_tax_thereon-tax_deduction
        if tax<0:
            tax=0
        return tax

class Couple:

    def __init__(self,case,hsal,wsal):
        self.case = case
        self.hsal = hsal
        self.wsal = wsal
        self.joint=False
        
    def taxation_choice(self):
        if((tax_payable(self.hsal)+tax_payable(self.wsal))>joint_tax(self.hsal,self.wsal)):
            method="Joint tax assessment"
            self.joint=True
        else:
            method="Tax sparately"
            self.joint=False
        return method
    
    def result(self,expected_joint=False):
        global total_case, successful_case
        total_case += 1
        result="Couple No."+str(self.case)+" should be using method:"+self.taxation_choice()+" as their better choice."
        print(result)
        if expected_joint==self.joint:
            print("The program did this case correctly!\n")
            successful_case += 1
        else:
            print("The program did not do this case correctly!\n")
            
    def print_detail(self):
        hnci=net_char_income_calculator(self.hsal)
        if hnci<0:
            hnci=0
        wnci=net_char_income_calculator(self.wsal)
        if wnci<0:
            wnci=0
        htt=tax_thereon(self.hsal)
        if htt<0:
            htt=0
        wtt=tax_thereon(self.wsal)
        if wtt<0:
            wtt=0
        print("Couple No."+str(self.case))
        print("husband year salary:"+str(self.hsal))
        print("wife year salary:"+str(self.wsal))
        print("husband chargable income:"+str(hnci))
        print("wife chargable income:"+str(wnci))
        print("husband tax thereon:"+str(htt))
        print("wife tax thereon:"+str(wtt))
        print("husband tax payable:"+str(tax_payable(self.hsal)))
        print("wife tax payable:"+str(tax_payable(self.wsal)))
        print("Sum of sparate taxation:"+str(tax_payable(self.wsal)+tax_payable(self.hsal)))
        print("Joint Tax:"+str(joint_tax(self.hsal,self.wsal))+"\n")
        

def Accuracy():
    global total_case, successful_case
    Accuracy='{:.1%}'.format(successful_case/total_case)
    print("The accuracy of this program is "+Accuracy+"! ("+str(total_case)+" case(s) has(have) been tested.)"+"\n")
    successful_case=0
    total_case=0

    
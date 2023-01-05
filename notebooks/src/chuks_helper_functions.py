import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# defining comparison barchart plot function

def compare_barchart_plot(dframe: pd.DataFrame, base_title: str, compare_title: str, xlabel: str, ylabel: str, independent_variable_of_interest: str, dependent_variable: str = "No-show", kind = "bar", figsize=(15, 15)):
    
    def format_compare_barchart(chart_title: str):
        plt.title(chart_title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        plt.show()
    
    (100 * dframe[independent_variable_of_interest].value_counts()/ dframe[independent_variable_of_interest].value_counts().sum()).plot(kind = kind, alpha = 0.5, rot = 0, label = "Population", color = "green", figsize=figsize)
    format_compare_barchart(base_title)
    
    (100 * dframe[dframe[dependent_variable]=="Yes"][independent_variable_of_interest].value_counts()/ dframe[dframe[dependent_variable]=="Yes"][independent_variable_of_interest].value_counts().sum()).plot(kind = kind, alpha = 0.5, label = f"{dependent_variable} = Yes", color = "red")
    (100 * dframe[dframe[dependent_variable]=="No"][independent_variable_of_interest].value_counts()/ dframe[dframe[dependent_variable]=="No"][independent_variable_of_interest].value_counts().sum()).plot(kind = kind, alpha = 0.5, rot = 0, label = f"{dependent_variable} = No", color = "blue", figsize=figsize)
    format_compare_barchart(compare_title)


# defining comparison histogram plot function

def compare_histogram_plot(dframe: pd.DataFrame, chart_title: str, continuous_independent_variable_of_interest: str, dependent_variable: str = "No-show", bins = 7, figsize=(15, 15)):
    dframe[continuous_independent_variable_of_interest].hist(bins = bins, alpha = 0.5, label = "Population", color = "green")
    dframe[continuous_independent_variable_of_interest][dframe[dependent_variable]=="Yes"].hist(bins = bins, alpha = 0.5, label = f"{dependent_variable} = Yes", color = "red")
    dframe[continuous_independent_variable_of_interest][dframe[dependent_variable]=="No"].hist(bins = bins, alpha = 0.5, label = f"{dependent_variable} = No", color = "blue", figsize=figsize)
    plt.title(chart_title)
    plt.xlabel(continuous_independent_variable_of_interest)
    plt.ylabel("Number of Patients")
    plt.legend()
    plt.show()


# defining comparison scatter plot function

def plot_scatter(dframe: pd.DataFrame, chart_title: str, continuous_independent_variable_of_interest: str, dependent_variable: str = "No-show", dependent_variable_int: str = "No-show-codes"):
    
    sns.scatterplot(data=dframe[[continuous_independent_variable_of_interest, dependent_variable, dependent_variable_int]], x = continuous_independent_variable_of_interest, y = dependent_variable_int, hue = dependent_variable, alpha = 0.7)
    plt.title(chart_title)
    plt.show()

    print(f"Correlation observed between the two variables is: {abs(dframe[continuous_independent_variable_of_interest].corr(dframe[dependent_variable_int])):.4f} or {abs(dframe[continuous_independent_variable_of_interest].corr(dframe[dependent_variable_int])) * 100:.2f}%")


# defining function for chi-square statistical test

def perform_chi_square_test(dframe: pd.DataFrame, independent_variable: str, dependent_variable_int: str, alpha = 0.05):
    from scipy.stats import chi2_contingency
  
    # defining the table
    focus_variables = pd.crosstab(dframe[independent_variable], dframe[dependent_variable_int], margins=True)

    display(focus_variables)

    # performing the chi-squared analysis
    stat, p, dof, expected = chi2_contingency(np.array([focus_variables.iloc[0][:].values, focus_variables.iloc[1][:].values]))
    
    # setting the level of significance (alpha) to serve as threshold against the p-value
    alpha = alpha
    
    print(f"p value is {str(p)}\n")
    if p <= alpha:
        print('\nThere is a statistically significant relationship between the two variables (reject H0)')
    else:
        print('\nThere is no statistically significant relationship between the two variables (H0 holds true)')




if __name__ == "__main__":
    print("Choose a function within this module to execute")
    print("Available functions are as follows: compare_barchart_plot, compare_histogram_plot, plot_scatter, perform_chi_square_test")
% Statistics for Linguists (LIN 538)

# Course Information

**Course:** TThu 15:00-16:20, SBS N310

**Instructor:** [Jeffrey Heinz](http://jeffreyheinz.net/), [jeffrey.heinz@stonybrook.edu](mailto:jeffrey.heinz@stonybrook.edu)

**Office Hours:** TThu 12:30-14:00, SBS N237

# Materials

* [Syllabus](materials/syllabus-stats-LIN538-22S-Heinz.pdf)
* Books we are using:
  * [Franke 2021](https://michael-franke.github.io/intro-data-analysis/index.html)
  * [Sonderegger 2022](http://osf.io/pnumg)

# Course Log

## 26 Apr 2022

* We determined the order of the presentations of the following papers for next week.
  - [Durvasula and Nelson 2020](https://www.sciencedirect.com/science/article/abs/pii/S0095447020301108)
  - [Kwon 2016](https://www.sciencedirect.com/science/article/abs/pii/S0095447016300869)
  - [Sprouse 2012](https://www.jonsprouse.com/papers/Sprouse%20et%20al.%202012a.pdf)
  - [Sprouse 2016](https://www.jonsprouse.com/papers/Sprouse%20et%20al.%202016.pdf)

* We discussed Mixed Effects Models (Sonderegger chapter 7).
  - Chadwick and Nelson's explainer ([pdf](materials/MixedEffectModels.pdf)) and ([rmd](materials/MixedEffectModels.Rmd)) files.

## 21 Apr 2022

* Class canceled.

## 19 Apr 2022

* We clarified any issues with the paper presentation.
* We finished issues with logistic regression (Sonderegger chapter 6).
* We briefly reviewed some aspects of Sonderegger chapter 7.

## 14 Apr 2022

* We continued discussion of logistic regression (Sonderegger chapter 6).
* We discussed the paper presentation you need to do in the last week of the course.

## 12 Apr 2022

* We discussed HW exercises in chapter 5.
* We began discussion of logistic regression (Sonderegger chapter 6).

## 07 Apr 2022

* We finished issues with linear regression (Sonderegger chapter 5).
* Homework for next Thursday: chapter 5, exercises 1-3 (page 172 in
  Sonderegger)

## 05 Apr 2022

* We discussed issues with linear regression (up to 5.6 in Sonderegger).

## 31 Mar 2022

* We spent the day exploring linear models of the preliminary
  NN/subregular lg data set.

## 29 Mar 2022

* We finished chapter 4 of Sonderegger.

## 24 Mar 2022

* We reviewed multiple linear regression (4.4 in Sonderegger).
* We discussed the NN/subreg data set.
* Homework for next Tuesday: Recall the Tati vowel data. Let us see
  how well we can predict the duration of a vowel from some its
  properties. Write a rmd file which conducts simple linear and
  multiple regressions to answer the following questions. For each
  regression conducted, make sure to present the summary (or tidy) of
  the model obtained, and include 1-2 sentences explaining what it
  means.
  1. Conduct a simple linear regression predicting the vowel duration from the F1.
  1. Conduct a simple linear regression predicting the vowel duration from the F2.
  1. Conduct a simple linear regression predicting the vowel duration from the pitch.
  1. Conduct a multiple linear regression predicting the vowel duration from the F1 + F2 + pitch.
  1. Conduct a simple linear regression predicting the vowel duration from the stress (S or U).
  1. Conduct a mulitple linear regression predicting the vowel duration from the Segment and stress.
  1. What are your overall conclusions about vowel duration in Tati?

## 22 Mar 2022

* We reviewed simple linear regression and this [fish
  example](materials/fish-lm.rmd).
* We discussed the NN/subreg data set.
* We began to look at regression with categorical variables.

## 10 Mar 2022

* We began discussion of regression. [Regression
  Handout](materials/regression.pdf)
* We covered the first couple of sections of Sonderegger chapter 4.

## 08 Mar 2022

* We discussed power and the incomplete neutralization example
  (chapter 3 section 3 of Sonderegger).
* For Thursday:
  - Using ggplot, draw a plot like the one in Figure 3.3 on page 61 of
	Sonderegger. As in Figure 3.3, the power should be plotted on the
	y-axis and sample size on the x-axis. However, instead of
	considering three effect sizes (5,10,30) just consider the effect
	size (delta) to be 10. And instead of considering fixing the
	standard deviation to 45ms, consider three possibilities: 15, 45,
	and 135. So your plot should have three lines in it like Figure
	3.3, but each one corresponding to one of the standard deviations
	instead of to the effect sizes.

## 03 Mar 2022

* We discussed effect size and the incomplete neutralization example
  (chapter 3 sections 1 and 2 of Sonderegger).
* For Tuesday:
  - Do exercise 1 in Sonderegger Chapter 3 (p.81)

## 01 Mar 2022

* Today we discussed z-tests, one-sample and two-saple t-tests,
  Wilcoxon tests, and checking normality.
* For Thursday:
  - Finish reading chapter 2 of Sonderegger.

## 24 Feb 2022

* We reviewed different kinds of probability distributions
  ([dists.rmd](materials/dists.rmd)).
* We reviewed standard error.
* We studied section 2.4 on hypothesis testing.
* For Tuesday:
  1. Do exercise 1 in Sonderegger Chapter 2 (p.44)
  2. Consider the Tati vowel data (will be sent in an email). Draw a
	 vowel plot with F1 and F2 values forming the axes.
  3. Conduct a Welch two sample t-test to see whether the mean heights
	 of the [i] and [u] vowels are equal. (Update: No need to to do
	 this one -- we will do in class on Tuesday)


## 22 Feb 2022

* We discussed the first part of Sonderegger Chapter 2.
* [Seeing Theory](https://seeing-theory.brown.edu/)
<!-- * https://stats.oarc.ucla.edu/r/modules/probabilities-and-distributions/ -->

## 17 Feb 2022

* We went over Franke chapter 6.
* For Tuesday 2/22: In a Rmarkdown file, load the [fish](materials/fishCatchData.csv) file, and write some R commmands to draw the following plots.
	1. Draw a bar chart showing the average weights of each kind of fish.
	2. Draw a histogram with 50 bins showing the weights of the fish. Color the different kinds of fish.
	2. Draw a boxplot showing the weights of the different kinds of fish.

## 15 Feb 2022

* We finished discussing covariance and correlation from Franke chapter 5.
* We discussed visualization including part of 6.3.
* For Thursday 2/17: finish reading 6.3, 6.4, and 6.5.

## 10 Feb 2022

* We went over Franke chapter 5.
* For Tuesday 2/15: In a Rmarkdown file, load the [fish](materials/fishCatchData.csv) and [nettle](materials/nettle_1999_climate.csv) files, and write some R commmands which answer the following questions.
	1. In `nettle`, what is the mean and standard deviation of the number of languages (per country)?
	2. In `nettle`, what the mean and standard deviation of the average Mean Growing Season (per country)?
	2. In `fish`, calculate the covariance and correlation for each *kind* of fish?
	2. In `fish`, change the weight and length of each fish to the imperial units (pounds and inches). Calculate the covariance and correlation for each *kind* of fish now. What has changed?


## 08 Feb 2022

* We went over the HW.
* We went over parts of [Franke](https://michael-franke.github.io/intro-data-analysis/index.html) chapters 3 and 4.

## 03 Feb 2022

* We went over Franke's 2.2. and 2.3 and studied anonymous functions and map functions.
* We went over some parts of Franke's chapter 4.
* For Tuesday 2/8: In a Rmarkdown file, load the [fish](materials/fishCatchData.csv) and [nettle](materials/nettle_1999_climate.csv) files, and write some R commmands which answer the following questions.
	1. In `nettle`, what are the minimum, maximum, and average number of languages (per country)?
	2. In `nettle`, what are the minimum, maximum, and average number the average Mean Growing Season (per country)?
	2. In `fish`, what are the minimum, maximum, and average weight for each *kind* of fish?
	2. In `fish`, what are the minimum, maximum, and average length for each *kind* of fish?
  (Hint: For #3 and #4, use the `group_by` and `summarize` commands in 4.4 of Franke.)

## 01 Feb 2022

* We went over the HW exercises.
* We reviewed sections 2.5, 2.6 and part of 2.4 of Franke.
* For Thursday 2/3:
  * Do the [R markdown tutorial](https://rmarkdown.rstudio.com/articles_intro.html)
  * Review 2.3 and 2.4 and come prepared with questions.
  * Review chapter 4 (at least 4.1 and 4.2 - I hope to also get to 4.3 on Thursday)

## 27 Jan 2022

* We discussed Chapter 1 of Sonderegger 2022.
* We reviewed Franke Section 2.1 and part of 2.2
* For Tuesday 2/1:
  * Complete [exercises 1.17.1 - 1.17.5](materials/exercises.pdf) from Winter 2019
  * Finish reading chapter 2 of [Franke 2021](https://michael-franke.github.io/intro-data-analysis/index.html).
  * Bring questions on Tuesday

## 25 Jan 2022

* We went over the syllabus.
* We talked about the course and our individual interests.
* For Thursday 1/27:
  * Install [R](https://cran.r-project.org/) and [R Studio](https://www.rstudio.com/products/rstudio/download/)
  * Open up RStudio and install the tidyverse in R: `install.packages('tidyverse')`
  * Read Chapter 1 of [Sonderegger 2022](http://osf.io/pnumg) (look for the file `rmld_V1.0.pdf` in the `output` folder).
  * Read Chapter 1 to section 2.3 of [Franke 2021](https://michael-franke.github.io/intro-data-analysis/index.html).


-------------------------------------------------------------------------------

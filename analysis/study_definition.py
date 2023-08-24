# https://docs.opensafely.org/study-def/#multiple-study-definitions
# https://docs.opensafely.org/study-def/#a-simple-example

# import some functions from the cohortextractor package which will be used throughout the script.
from cohortextractor import (
    StudyDefinition,
    #   codelist,
    #   codelist_from_csv,
    #   combine_codelists,
    #   filter_codes_by_category,
    patients,
)
# from cohortextractor import StudyDefinition, patients, codelist  #, codelist_from_csv  # NOQA


study = StudyDefinition(
    # default_expectations, index_date, and population arguments 
    #   are reserved names within StudyDefinition(). 
    #   All other names are used to define the variables that will 
    #   appear in the outputted dataset, 
    #   using variable extractor functions of the form 
    #       patients.function_name

    default_expectations={
        # expect event dates to be between 1970-01-01 and today's date,
        # uniformly distributed in that period,
        # recorded for 20% of patients (returning empty "" values otherwise).
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },
    # define the study population
    # population=patients.all(),
    # all patients available in the OpenSAFELY database
    #   so we use the method all() to indicate this
    # Be aware - includes mix of registered, deregistered, and deceased patients.



    # study definition must have a population variable defined. 
    # This is a special variable used to select all the patients 
    # for whom you want to extract information.
    # Most likely, there will be multiple criteria used to
    # include or exclude your study population,
    # in which case you'll need to combine information
    # from multiple different variables.
    # We can do this using the patients.satisfying() function.

    # population=patients.registered_with_one_practice_between(
    #    # all patients who have never changed practice, between these two dates
    #    "2019-02-01", "2020-02-01"
    # ),
    population=patients.satisfying(
        'has_follow_up AND (sex = "M" OR sex = "F")',
        has_follow_up=patients.registered_with_one_practice_between(
            "2019-03-01", "2020-03-01"
        ),
    ),
    sex=patients.sex(
        return_expectations={
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
            # https://docs.opensafely.org/study-def/#dummy-data-versus-real-data
            # incidence" : 0.95, then 5% of patients in the dummy data
            # would have missing sex values,
            # but 0% of patients in the real data would have missing sex values
            # because they have been excluded with population=.
            # It's important therefore to match the dummy data with
            # what you would expect to see conditional on the chosen patient population
            # rather than in the data as a whole.


            "incidence": 1,
        }
    ),

    # define the study index date
    # set the index date against which all other dates can be defined
    index_date="2020-01-01",

    # define the study variables
    # age is simple example of an extractor function
    #   The patients.age_as_of() function returns the
    #   age of each patient as of the date provided
    #       (in this case the index_date).
    age=patients.age_as_of(
        # column of data corresponding to the age of each patient
        # on the given date
        "index_date",
        # "2019-09-01",
        return_expectations={
            # every patient to have a value,
            # and the distribution of ages
            # to match that of the real UK population
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),

)

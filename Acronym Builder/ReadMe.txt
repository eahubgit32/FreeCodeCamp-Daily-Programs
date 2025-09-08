Acronym Builder
Given a string containing one or more words, return an acronym of the words using the following constraints:

The acronym should consist of the first letter of each word capitalized, unless otherwise noted.
The acronym should ignore the first letter of these words unless they are the first word of the given string: a, for, an, and, by, and of.
The acronym letters should be returned in order they are given.
The acronym should not contain any spaces.


Tests
Passed:1. build_acronym("Search Engine Optimization") should return "SEO".
Passed:2. build_acronym("Frequently Asked Questions") should return "FAQ".
Passed:3. build_acronym("National Aeronautics and Space Administration") should return "NASA".
Passed:4. build_acronym("Federal Bureau of Investigation") should return "FBI".
Passed:5. build_acronym("For your information") should return "FYI".
Passed:6. build_acronym("By the way") should return "BTW".
Passed:7. build_acronym("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily") should return "AUHWPOTIMSH".

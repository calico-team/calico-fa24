sed -i "s/\(PROBLEM_NAME = '[^']*\)'/\1_final'/" make_zips.py && rm *.zip && ./make_data.py && ./make_zips.py

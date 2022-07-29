# Remove extra line break from multiple rows in table.
find ./docs/sphinx/build/html -type f -name "*.html" | xargs -I%% sed -i -e 's/<td><div class="line-block">/<td><div>/g' %%

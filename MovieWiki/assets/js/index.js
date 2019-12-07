function validate(search_value) {
    if (search_value === '') {
        alert('Please enter a valid movie');
        return false;
    } return true;
}
async function searchMovieAPI() {
    let search_value = document.getElementById('search-value').value;

    if (validate(search_value)) {
        let search_url = 'http://www.omdbapi.com/?apikey=7ac167cf&s=' + search_value;
        let json_data = await fetch(search_url).then(function (response) {
            return response.json();
        }).then(function (returnedValue) {
            return returnedValue['Search'];
            //console.log(returnedValue);
        }).catch(function (err) {
            // Error :(
            console.error(err);
        });

        json_data.forEach(element => {
            console.log(element['Title']);
        });
        window.location.assign('search.html');
        
    }

}
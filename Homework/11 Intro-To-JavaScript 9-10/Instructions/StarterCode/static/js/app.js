// from data.js
var tableData = data;

console.log(data);

// YOUR CODE HERE!
// add data to the table by defining a function rendertable that inputs the data and adds a each row to the table
function rendertable(datarow){
	// iterate through data and build the HTML table
//console.log('In Rendertable',datarow);
 var tbody = d3.select("tbody");
  var row = tbody.append("tr");

  Object.entries(datarow).forEach(([key, value]) => {
    
    var cell = tbody.append("td");
    
    cell.text(value);
  });

}
// Display the entire dataset as default
tableData.forEach(rendertable);

// Part 1: Use a date form in your HTML document and write JavaScript code that will listen for events and search through the date/time column to find rows that match user input.

// // Click event of datetime filter
//filterbutton.on("click", function() {

//     // Remove existing table
// 	d3.select("tbody").html("");

   // Prevent the page from refreshing
//d3.event.preventDefault();

//     // Get the value property of the input element
// var dateTime = d3.select("#datetime").property("value");
//  console.log(dateTime);

//     // Filter reports
//  var filteredData = tableData.filter(record => record.datetime === dateTime);
//    console.log(filteredData)

 

//     // Display the filtered dataset

//   filteredData.forEach(rendertable);


// });

/// Part 2: Using multiple input tags and/or select dropdowns, write JavaScript code so the user can set multiple filters 
//and search for UFO sightings using the following criteria based on the table columns: date/time, city, state, country, shape

//assign a variable to the filter button
var filterbutton = d3.select("#filter-btn");


//upon clicking the filter button on the the screen
filterbutton.on("click", function() {

// Remove existing table
	d3.select("tbody").html("");

// Prevent the page from refreshing
	d3.event.preventDefault();

// Get the value property of the input element entered


var filteredDate = d3.select("#datetime").property("value");
console.log(`date: ${filteredDate}`);

var state = d3.select("#state").property("value").toLowerCase();
console.log(`state: ${state}`);

var city = d3.select("#city").property("value").toLowerCase();
console.log(`city: ${city}`);

var country = d3.select("#country").property("value").toLowerCase();
console.log(`country: ${country}`);

var shape = d3.select("#shape").property("value").toLowerCase();
console.log(`shape: ${shape}`);

var filteredData = tableData;

// assign the filtered value into a key value pair that can be passed to the render table function
function filteredValue(data, key, result)
{
	console.log('Incoming Data',data);
	console.log('Key value',key);
	var filteredData = data.filter(record => record[key] === result);
	console.log('Filetered value',filteredData);
	return filteredData;
}

//conditions for each filter criteria

if(filteredDate !=""){
filteredData = filteredValue(filteredData, 'datetime', filteredDate)
   console.log('filter data',filteredData) ;
};



if((country !=='all') && (country !== ''))
{
	filteredData= filteredValue(filteredData,'country',country)

};

if((state !=='N' ) && (state !== ''))
{
	//console.log('I am executed',typeof state)
	filteredData= filteredValue(filteredData,'state',state)

};

if((city !=='N') && (city !== ''))
{
	filteredData= filteredValue(filteredData,'city',city)

};

if((shape !=='N') && (shape !== ''))
{
	filteredData= filteredValue(filteredData,'shape',shape)
	console.log('Filtered Data in Shape',filteredData);

};

//Call the render table function.
//console.log('Filetered data before call',filteredData)
filteredData.forEach(rendertable);

    
});
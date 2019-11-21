var data = [
  {name: "Clothing and Textiles", value: 19},
  {name: "Electronics, Computers and Transportation", value: 74},
  {name: "Food Production", value: 234},
  {name: "Metal Manufacturing", value: 29},
  {name: "Misc", value: 46},
  {name: "Petrolium, Chemicals and Plastics", value: 18},
  {name: "Wood, Leather and Paper", value: 77}
];
var text = "";

var width2 = 260;
var height2 = 260;
var thickness = 40;
var duration = 750;

var radius = Math.min(width2, height2) / 2;
var color = d3.scaleOrdinal(d3.schemeCategory10);

var svg2 = d3.select("#piechart")
.append('svg')
.attr('class', 'pie')
.attr('width', width2)
.attr('height', height2);


var g = svg2.append('g')
.attr('transform', 'translate(' + (width2/2) + ',' + (height2/2) + ')');

var arc = d3.arc()
.innerRadius(radius - thickness)
.outerRadius(radius);

var pie = d3.pie()
.value(function(d) { return d.value; 

})
.sort(null);


var path2 = g.selectAll('path')
.data(pie(data))
.enter()
.append("g")
.on("mouseover", function(d) {
      let g = d3.select(this)
        .style("cursor", "pointer")
        .style("fill", "black")
        .append("g")
        .attr("class", "text-group");
 
      g.append("text")
        .attr("class", "name-text")
        .text(`${d.data.name}`)
        .attr('text-anchor', 'middle')
        .attr('dy', '-1.2em');
  
      g.append("text")
        .attr("class", "value-text")
        .text(`${d.data.value}`)
        .attr('text-anchor', 'middle')
        .attr('dy', '.6em');


    })
  .on("mouseout", function(d) {
      d3.select(this)
        .style("cursor", "none")  
        .style("fill", color(this._current))
        .select(".text-group").remove();
    })
  .append('path')
  .attr('d', arc)
  .attr('fill', (d,i) => color(i))
  .on("mouseover", function(d) {
      d3.select(this)     
        .style("cursor", "pointer")
        .style("fill", "black");
    })
  .on("mouseout", function(d) {
      d3.select(this)
        .style("cursor", "none")  
        .style("fill", color(this._current));
    })
  .each(function(d, i) { this._current = i; });


g.append('text')
  .attr('text-anchor', 'middle')
  .attr('dy', '.35em')
  .text(text);
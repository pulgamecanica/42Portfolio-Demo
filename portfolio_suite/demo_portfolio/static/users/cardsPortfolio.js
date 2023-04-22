const svgHeight = 300, svgWidth = 600;
const data = document.currentScript.dataset;
const user = JSON.parse(data.user);

console.log(user)

const drawCircles2 = (svg, circles) => {
  svg.selectAll( "circle" )
    .data( circles ).enter().append( "circle" )
    .attr( "r", d => d["r"] )
    .attr( "cx", d => d["cx"] )
    .attr( "cy", d => d["cy"] )
    .attr( "fill", d => d["color"] );
}

window.addEventListener("load", () => {
  const svg = d3.select( "#content" ).append( "svg" )
    .attr( "id", "drag-drop")

  console.log(svg)

  d3.selectAll( "svg" )
    .attr( "width", svgWidth )
    .attr( "height", svgHeight );

  let circles = [
    {r: 20, color: "red", cx: 50, cy: 100},
    {r: 20, color: "green", cx: 250, cy: 150},
    {r: 20, color: "blue", cx: 350, cy: 100}
  ];
  drawCircles2( svg, circles );

  let color = undefined, widget = undefined;
  
  svg.selectAll( "circle" )
    .call( d3.drag()
        .on( "start", function () {
          color = d3.select( this ).attr( "fill" );
          widget = d3.select( this ).attr( "fill", "lime" );
        } )
        .on( "drag", function () {
          let pt = d3.pointer( event, this );
          widget.attr( "cx", pt[0] ).attr( "cy", pt[1] )
        } )
        .on( "end", function () {
          widget.attr( "fill", color );
          widget = undefined;
          color = undefined;
        } )
    );
});


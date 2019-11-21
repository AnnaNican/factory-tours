const svg5 = document.querySelector('.bar-chart');

new chartXkcd.Bar(svg5, {
  // title: 'github stars VS patron number', // optional
  // xLabel: '', // optional
  // yLabel: '', // optional
  data: {
    labels: ['github stars', 'patrons'],
    datasets: [{
      data: [5, 2],
    }],
  },
  options: { // optional
    yTickCount: 2,
  },
});
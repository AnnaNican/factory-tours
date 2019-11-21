  const svg1 = document.querySelector('.radar-chart');
  
  const radarChart = new chartXkcd.Radar(svg1, {
    // title: 'Top States with Factory tours',
    data: {
      labels: ['California', 'Pennsylvania', 'Wisconsin', 'Ohio', 'Indiana', 'Vermont', 'North Carolina', 'Texas', 'New York', 'Oregon'],
      datasets: [{
        label: 'Clothing and Textiles',
        data: [2, 1, 0, 2, 0, 1, 1, 3, 1, 1],
      }, {
        label: 'Electronics Computers and Transportation',
        data: [5, 2, 4, 1, 9, 0, 12, 4, 0, 2],
      },
      {
        label: 'Food',
        data: [22, 25, 20, 12, 6, 13, 1, 9, 3, 8],
      },
      {
        label: 'Metal',
        data: [2, 2, 2, 2, 0, 1, 0, 0, 1, 0],
      },
      {
        label: 'Misc',
        data: [10, 4, 1, 0, 0, 0, 1, 0, 7, 3],
      },
      {
        label: 'Petrolium, Chemicals and Plastics',
        data: [1, 3, 4, 2, 2, 0, 0, 0, 0, 0],
      },
      {
        label: 'Wood, Leather and Paper',
        data: [10, 6, 1, 4, 5, 5, 4, 2, 6, 3],
      }
      ],
    },
    options: {
      showLegend: false,
      dotSize: 0.8,
      showLabels: true, 
      dataColors: ['#F9FA74', '#D82E20', '#98ACE3', '#9FC55C', '#F5B85A', '#53B9D7']
      // legendPosition: chartXkcd.config.positionType.upRight,
      // unxkcdify: true,
    },

  });
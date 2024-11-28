module.exports = {
    devServer: {
      host: '0.0.0.0',
      port: process.env.VUE_APP_PORT || 8080,
      allowedHosts: ['all']
    }
  };
  
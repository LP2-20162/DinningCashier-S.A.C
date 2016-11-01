app

//algo
.config(function($stateProvider, $urlRouterProvider) {

  $stateProvider

    .state('test', {
      url: "/testx",
      templateUrl: "dinning_Cashier_web_apps/catalogo_web/views/test/index.html"
    })


    .state('form', {
      url: "/formx",
      templateUrl: "dinning_Cashier_web_apps/catalogo_web/views/form/index.html"
    });

});
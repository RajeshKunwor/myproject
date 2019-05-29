function ModelView(){
    var self = this;
    self.medicineArray = ko.observableArray();
    var cur_date = new Date()
    var fullyear = cur_date.getFullYear();
    var month = cur_date.getMonth()+1;
    var day = cur_date.getDate();
    var c_date = (fullyear+"-"+month+"-"+day)
    var url = $("table").attr("url");
    var status = ''
    $.get(url, function(data){

        for (var i in data){
            var ed = data[i].expiry_date;
            var ed1 = new Date(ed)
            var d2 = new Date(c_date)

            var dd = ed1.getTime()-d2.getTime()
            var day = Math.floor(dd/(1000*3600*24))
            self.medicineArray.push({ id: data[i].id, name: data[i].name, quantity: data[i].quatity,
            manufacture_date: data[i].manufacture_date, expiry_date: data[i].expiry_date, expiry_day: day});
        }
        console.log(self.medicineArray())


    });



}

ko.applyBindings(new ModelView());
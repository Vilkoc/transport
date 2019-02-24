from django.db import models
#module_name, package_name, ClassName, method_name, ExceptionName,
##  function_name, GLOBAL_CONSTANT_NAME, global_var_name,
# instance_var_name, function_parameter_name, local_var_name
class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    role = models.IntegerField(default=1)

class Place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    lat = models.FloatField()
    lng = models.FloatField()

class Bus_stop(models.Model):
    name = models.CharField(max_length=40)
    lat = models.FloatField()
    lng = models.FloatField()
    '''def nearest(self, lata, lnga, quantiti):
        return self.objects.annotate(abs_lat=Func(F('lng') - lnga, function='ABS')).annotate(
            abs_lit=Func(F('lit') - lata, function='ABS')).annotate(all_diff=F('abs_lat') + F('abs_lit')).order_by(
            'all_diff').all()[:quantiti]
        self.objects.annotate(abs_diff=Func(F('lat') - 49, function='ABS')).order_by('abs_diff').first()
        self.objects.annotate(abs_diff=Func(F(Func(F('lat') - 49, function='ABS')).order_by('abs_diff').first()
        sql = 'SELECT * FROM bus_stop ORDER BY (ABS(lat - %s) - ABS(lit - %s)), [self.lat, self.lit]'
        self.objects.raw('SELECT * FROM transport_bus_stop ORDER BY ABS(ABS(lat - %s) - ABS(lit - %s))', [self.lat, self.lit])
        a = Bus_stop.objects.annotate(abs_lat=Func(F('lat') - la, function='ABS')).annotate(abs_lit=Func(F('lit') - li, function='ABS')).annotate(all_diff = F('abs_lat') + F('abs_lit')).order_by('all_diff').all()
        '''

class Bus_route(models.Model):
    route = models.CharField(max_length=3)

class Bus_stop_position(models.Model):
    stop = models.ForeignKey(Bus_stop, on_delete=models.CASCADE)
    route = models.ForeignKey(Bus_route, on_delete=models.CASCADE)
    position = models.IntegerField()
    length = models.IntegerField()

class Route_way(models.Model):
    route = models.ForeignKey(Bus_route, on_delete=models.CASCADE)
    position = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()


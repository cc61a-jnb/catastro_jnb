# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class UsuCargo(models.Model):
    carg_id = models.IntegerField(primary_key=True)
    carg_nombre = models.IntegerField()
    id_usu = models.IntegerField()
    carg_prioridad = models.TextField() # This field type is a guess.
    carg_cuerpo_id = models.IntegerField()
    carg_fechaini = models.DateField()
    carg_fechafin = models.DateField()
    class Meta:
        db_table = u'usu_cargo'

class Usuarios(models.Model):
    usu_id = models.IntegerField(primary_key=True)
    usu_nombre = models.CharField(max_length=45)
    usu_ape_pat = models.CharField(max_length=50)
    usu_ape_mat = models.CharField(max_length=50)
    usu_rut = models.CharField(max_length=15)
    usu_dv = models.CharField(max_length=255)
    usu_claves = models.IntegerField()
    usu_direccion = models.CharField(max_length=60)
    usu_telefono = models.CharField(max_length=15)
    usu_celular = models.CharField(max_length=15)
    usu_foto = models.TextField() # This field type is a guess.
    usu_ocupacion = models.CharField(max_length=50)
    usu_fono_laboral = models.CharField(max_length=15)
    usu_direc_laboral = models.CharField(max_length=50)
    usu_fk_cia = models.IntegerField()
    usu_fk_perfil = models.IntegerField()
    usu_fk_cargo = models.IntegerField()
    usu_fk_cuerpo = models.IntegerField()
    usu_fk_reg = models.IntegerField()
    usu_fk_sexo = models.TextField() # This field type is a guess.
    usu_tipo_usuario = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'usuarios'

class 5(models.Model):
    usu_nombre = models.CharField(max_length=45)
    usu_ape_mat = models.CharField(max_length=50)
    usu_ape_pat = models.CharField(max_length=50)
    class Meta:
        db_table = u'5'

class Cargo(models.Model):
    cargo_id = models.IntegerField()
    cargo_nombre = models.CharField(max_length=-1)
    cargo_prioridad = models.IntegerField()
    cargo_lugar = models.IntegerField()
    class Meta:
        db_table = u'cargo'

class Cuerpos(models.Model):
    cuer_id = models.IntegerField(primary_key=True)
    cuer_nombre = models.CharField(max_length=150)
    cuer_rut = models.CharField(max_length=-1)
    cuer_fk_region = models.IntegerField()
    cuer_direccion = models.CharField(max_length=150)
    cuer_comuna = models.CharField(max_length=45)
    cuer_telefono = models.CharField(max_length=40)
    cuer_fax = models.CharField(max_length=40)
    cuer_casilla = models.CharField(max_length=15)
    cuer_mail = models.CharField(max_length=45)
    cuer_pag_web = models.CharField(max_length=75)
    cuer_fecha_fund = models.CharField(max_length=45)
    cuer_lema = models.CharField(max_length=150)
    cuer_central_alarmas = models.CharField(max_length=45)
    cuer_comunas_atend = models.CharField(max_length=65)
    cuer_logo = models.TextField() # This field type is a guess.
    cuer_npers_juri = models.CharField(max_length=-1)
    cuer_fech_decre = models.CharField(max_length=-1)
    cuer_provin = models.IntegerField()
    comp_id = models.IntegerField()
    comp_nro = models.IntegerField()
    comp_nombre = models.CharField(max_length=255)
    comp_fk_cuerpo = models.IntegerField()
    comp_rut_cuerpo_pertenece = models.CharField(max_length=255)
    comp_telefono = models.CharField(max_length=255)
    comp_mail = models.CharField(max_length=255)
    comp_logo = models.CharField(max_length=255)
    comp_direccion = models.CharField(max_length=255)
    comp_comuna = models.CharField(max_length=255)
    comp_fax = models.CharField(max_length=255)
    comp_casilla = models.CharField(max_length=255)
    comp_sitioweb = models.CharField(max_length=255)
    comp_calarmas = models.CharField(max_length=255)
    comp_lema = models.CharField(max_length=255)
    comp_especialidad = models.CharField(max_length=255)
    comp_comunasatendidas = models.CharField(max_length=255)
    comp_ffundacion = models.CharField(max_length=255)
    comp_fk_comuna = models.IntegerField()
    class Meta:
        db_table = u'cuerpos'

class VistaUsuCargoCuerpoCia(models.Model):
    usu_id = models.IntegerField()
    nombre = models.CharField(max_length=45)
    ape_pat = models.CharField(max_length=50)
    ape_mat = models.CharField(max_length=50)
    fk_cia = models.IntegerField()
    fk_cpo = models.IntegerField()
    cargo_id = models.IntegerField()
    cargo_nombre = models.CharField(max_length=-1)
    cuer_id = models.IntegerField()
    cuerpo = models.CharField(max_length=150)
    region = models.IntegerField()
    class Meta:
        db_table = u'VISTA_USU_CARGO_CUERPO_CIA'

class Acciones(models.Model):
    correlativo = models.IntegerField()
    codresponsable = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    tipoestado = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=256)
    fecha = models.DateField()
    hora = models.TimeField()
    cuer_id = models.IntegerField()
    comp_id = models.IntegerField()
    idarticulo = models.IntegerField()
    usu_id = models.IntegerField()
    usu_nombre = models.CharField(max_length=45)
    usu_ape_pat = models.CharField(max_length=45)
    usu_ape_mat = models.CharField(max_length=45)
    class Meta:
        db_table = u'acciones'

class Cargo1(models.Model):
    usu_fk_cia = models.IntegerField()
    usu_fk_cuerpo = models.IntegerField()
    class Meta:
        db_table = u'cargo1'

class CargoNew(models.Model):
    cargo_id = models.IntegerField()
    cargo_nombre = models.CharField(max_length=-1)
    cargo_prioridad = models.IntegerField()
    cargo_lugar = models.IntegerField()
    class Meta:
        db_table = u'cargo_new'

class CargoPorUsuario(models.Model):
    cargo_id = models.IntegerField()
    cargo_nombre = models.CharField(max_length=-1)
    cargo_prioridad = models.IntegerField()
    cargo_lugar = models.IntegerField()
    carg_id = models.IntegerField()
    carg_nombre = models.IntegerField()
    id_usu = models.IntegerField()
    carg_cuerpo_id = models.IntegerField()
    usu_id = models.IntegerField()
    usu_nombre = models.CharField(max_length=-1)
    usu_ape_pat = models.CharField(max_length=-1)
    usu_ape_mat = models.CharField(max_length=-1)
    usu_rut = models.CharField(max_length=-1)
    usu_dv = models.CharField(max_length=-1)
    usu_fk_cuerpo = models.IntegerField()
    usu_fk_cia = models.IntegerField()
    cuer_id = models.IntegerField()
    cuer_nombre = models.CharField(max_length=-1)
    comp_id = models.IntegerField()
    comp_nro = models.IntegerField()
    comp_nombre = models.CharField(max_length=-1)
    class Meta:
        db_table = u'cargo_por_usuario'

class CargoPorUsuario2(models.Model):
    carg_id = models.IntegerField()
    carg_nombre = models.IntegerField()
    id_usu = models.IntegerField()
    carg_cuerpo_id = models.IntegerField()
    cargo_id = models.IntegerField()
    cargo_nombre = models.CharField(max_length=-1)
    cargo_prioridad = models.IntegerField()
    cargo_lugar = models.IntegerField()
    class Meta:
        db_table = u'cargo_por_usuario2'

class CargoPorUsuario3(models.Model):
    carg_id = models.IntegerField()
    carg_nombre = models.IntegerField()
    id_usu = models.IntegerField()
    carg_cuerpo_id = models.IntegerField()
    cargo_id = models.IntegerField()
    cargo_nombre = models.CharField(max_length=-1)
    cargo_prioridad = models.IntegerField()
    cargo_lugar = models.IntegerField()
    usu_nombre = models.CharField(max_length=-1)
    usu_ape_pat = models.CharField(max_length=-1)
    usu_ape_mat = models.CharField(max_length=-1)
    usu_rut = models.CharField(max_length=-1)
    usu_dv = models.CharField(max_length=-1)
    usu_fk_cia = models.IntegerField()
    usu_fk_cuerpo = models.IntegerField()
    class Meta:
        db_table = u'cargo_por_usuario3'

class CiasImagen(models.Model):
    id_cia_imagen = models.IntegerField(primary_key=True)
    id_fkcia_imagen = models.IntegerField()
    nombre_imagen = models.CharField(max_length=150)
    class Meta:
        db_table = u'cias_imagen'

class Ciudades(models.Model):
    ciud_id = models.IntegerField(primary_key=True)
    ciud_nombre = models.CharField(max_length=35)
    ciud_fk_region = models.IntegerField()
    class Meta:
        db_table = u'ciudades'

class Compania(models.Model):
    comp_id = models.IntegerField(primary_key=True)
    comp_nombre = models.CharField(max_length=256)
    comp_fk_cuerpo = models.IntegerField()
    class Meta:
        db_table = u'compania'

class Companias2(models.Model):
    comp_id = models.IntegerField()
    comp_nro = models.IntegerField()
    comp_nombre = models.CharField(max_length=45)
    comp_fk_cuerpo = models.IntegerField()
    comp_rut_cuerpo_pertenece = models.CharField(max_length=-1)
    comp_telefono = models.CharField(max_length=-1)
    comp_mail = models.CharField(max_length=-1)
    comp_logo = models.CharField(max_length=255)
    comp_direccion = models.CharField(max_length=-1)
    comp_comuna = models.CharField(max_length=-1)
    comp_fax = models.CharField(max_length=-1)
    comp_casilla = models.CharField(max_length=-1)
    comp_sitioweb = models.CharField(max_length=-1)
    comp_calarmas = models.CharField(max_length=-1)
    comp_lema = models.CharField(max_length=-1)
    comp_especialidad = models.CharField(max_length=-1)
    comp_comunasatendidas = models.CharField(max_length=-1)
    comp_ffundacion = models.CharField(max_length=-1)
    comp_fk_comuna = models.IntegerField()
    class Meta:
        db_table = u'companias2'

class Comuna(models.Model):
    comu_ide = models.IntegerField()
    comu_nombre = models.CharField(max_length=-1, primary_key=True)
    comu_fk_region = models.CharField(max_length=-1)
    comu_url = models.CharField(max_length=255)
    prov_id = models.IntegerField()
    class Meta:
        db_table = u'comuna'

class ComunasAtenComp(models.Model):
    id_url = models.IntegerField()
    id_comp = models.IntegerField()
    id_comuna = models.IntegerField()
    class Meta:
        db_table = u'comunas_aten_comp'

class ComunasAtendidas(models.Model):
    id_url = models.IntegerField()
    id_cuerpo = models.IntegerField()
    id_comuna = models.IntegerField()
    class Meta:
        db_table = u'comunas_atendidas'

class CuerposImagen(models.Model):
    id_cpo_imagen = models.IntegerField(primary_key=True)
    id_fkcpo_imagen = models.IntegerField(unique=True)
    nombre_imagen = models.CharField(max_length=150)
    class Meta:
        db_table = u'cuerpos_imagen'

class CuerposOld(models.Model):
    cuer_id = models.IntegerField(primary_key=True)
    cuer_nombre = models.CharField(max_length=45)
    cuer_rut = models.CharField(max_length=-1)
    cuer_fk_region = models.IntegerField()
    cuer_direccion = models.CharField(max_length=75)
    cuer_comuna = models.CharField(max_length=45)
    cuer_telefono = models.CharField(max_length=40)
    cuer_fax = models.CharField(max_length=40)
    cuer_casilla = models.CharField(max_length=15)
    cuer_mail = models.CharField(max_length=45)
    cuer_pag_web = models.CharField(max_length=75)
    cuer_fecha_fund = models.CharField(max_length=45)
    cuer_lema = models.CharField(max_length=150)
    cuer_central_alarmas = models.CharField(max_length=45)
    cuer_comunas_atend = models.CharField(max_length=65)
    cuer_logo = models.TextField() # This field type is a guess.
    cuer_npers_juri = models.CharField(max_length=-1)
    cuer_fech_decre = models.CharField(max_length=-1)
    cuer_provin = models.IntegerField()
    class Meta:
        db_table = u'cuerpos_old'

class Duplicados(models.Model):
    ?column? = models.BooleanField()
    class Meta:
        db_table = u'duplicados'

class Estado(models.Model):
    est_id = models.IntegerField()
    est_nombre = models.CharField(max_length=80)
    class Meta:
        db_table = u'estado'

class Ficha(models.Model):
    cuer_id = models.IntegerField()
    usu_nombre = models.CharField(max_length=45)
    usu_ape_mat = models.CharField(max_length=50)
    usu_ape_pat = models.CharField(max_length=50)
    usu_fk_cuerpo = models.IntegerField()
    usu_dv = models.CharField(max_length=255)
    usu_id = models.IntegerField()
    usu_rut = models.CharField(max_length=15)
    comp_fk_cuerpo = models.IntegerField()
    class Meta:
        db_table = u'ficha'

class Funcionarios(models.Model):
    prac_id = models.IntegerField(primary_key=True)
    prac_rut = models.CharField(max_length=255)
    prac_fono = models.IntegerField()
    edad = models.CharField(max_length=255)
    prac_nom = models.CharField(max_length=255)
    class Meta:
        db_table = u'funcionarios'

class IndicEcono(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    uf = models.CharField(max_length=-1)
    utm = models.CharField(max_length=-1)
    dolar = models.CharField(max_length=-1)
    euro = models.CharField(max_length=-1)
    class Meta:
        db_table = u'indic_econo'

class Mailbox(models.Model):
    username = models.CharField(max_length=256, primary_key=True)
    password = models.CharField(max_length=256)
    correopk = models.IntegerField()
    class Meta:
        db_table = u'mailbox'

class Marca(models.Model):
    mar_id = models.IntegerField()
    mar_nombre = models.CharField(max_length=80)
    class Meta:
        db_table = u'marca'

class MaterialMayor(models.Model):
    reg_id = models.IntegerField()
    reg_id_marca = models.IntegerField()
    reg_modelo = models.CharField(max_length=255)
    reg_id_condicion = models.IntegerField()
    reg_fecha_entrega = models.DateField()
    reg_anho = models.IntegerField()
    reg_patente = models.CharField(max_length=10)
    reg_id_tipo = models.IntegerField()
    reg_chasis = models.CharField(max_length=250)
    reg_motor = models.CharField(max_length=250)
    reg_procedencia = models.IntegerField()
    reg_otra_procedencia = models.CharField(max_length=255)
    reg_id_estado = models.IntegerField()
    reg_otro_estado = models.CharField(max_length=255)
    reg_cuerpo = models.IntegerField()
    reg_cia = models.IntegerField()
    reg_observacion = models.CharField(max_length=500)
    reg_foto = models.CharField(max_length=255)
    reg_fecha_reasignacion = models.DateField()
    class Meta:
        db_table = u'material_mayor'

class NroSistemas(models.Model):
    nro_id = models.IntegerField(primary_key=True)
    nro_nombre = models.CharField(unique=True, max_length=30)
    class Meta:
        db_table = u'nro_sistemas'

class Perfil(models.Model):
    perf_id = models.IntegerField(primary_key=True)
    perf_mail = models.CharField(max_length=65)
    perf_password = models.CharField(max_length=45)
    perf_nivel = models.IntegerField()
    perf_permiso = models.CharField(max_length=5)
    class Meta:
        db_table = u'perfil'

class PersoUrl(models.Model):
    ide_perso_url = models.IntegerField(primary_key=True)
    nom_perso_url = models.CharField(max_length=-1)
    dir_perso_url = models.CharField(max_length=-1)
    idusu_perso_url = models.IntegerField()
    class Meta:
        db_table = u'perso_url'

class PgaDiagrams(models.Model):
    diagramname = models.CharField(max_length=64, primary_key=True)
    diagramtables = models.TextField()
    diagramlinks = models.TextField()
    class Meta:
        db_table = u'pga_diagrams'

class PgaForms(models.Model):
    formname = models.CharField(max_length=64, primary_key=True)
    formsource = models.TextField()
    class Meta:
        db_table = u'pga_forms'

class Estadoarticulos(models.Model):
    cuer = models.ForeignKey(Estados)
    comp_id = models.IntegerField()
    idarticulo = models.IntegerField()
    codtipoestado = models.CharField(max_length=40)
    codestado = models.CharField(max_length=40)
    motivo = models.CharField(max_length=256)
    fechahora = models.DateField()
    codresponsable = models.ForeignKey(Responsables, db_column='codresponsable')
    class Meta:
        db_table = u'estadoarticulos'

class Localizaciones(models.Model):
    cuer = models.ForeignKey(Tipodelocalizacion)
    comp_id = models.IntegerField()
    codtipoloc = models.CharField(max_length=40)
    codigo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=256)
    estadolocalizacion = models.BooleanField()
    codtipoloc1 = models.CharField(max_length=40)
    codlocalizacion1 = models.CharField(max_length=40)
    cuer_id1 = models.IntegerField()
    comp_id1 = models.IntegerField()
    class Meta:
        db_table = u'localizaciones'

class PgaGraphs(models.Model):
    graphname = models.CharField(max_length=64, primary_key=True)
    graphsource = models.TextField()
    graphcode = models.TextField()
    class Meta:
        db_table = u'pga_graphs'

class PgaImages(models.Model):
    imagename = models.CharField(max_length=64, primary_key=True)
    imagesource = models.TextField()
    class Meta:
        db_table = u'pga_images'

class PgaLayout(models.Model):
    tablename = models.CharField(max_length=64, primary_key=True)
    nrcols = models.SmallIntegerField()
    colnames = models.TextField()
    colwidth = models.TextField()
    class Meta:
        db_table = u'pga_layout'

class PgaQueries(models.Model):
    queryname = models.CharField(max_length=64, primary_key=True)
    querytype = models.TextField() # This field type is a guess.
    querycommand = models.TextField()
    querytables = models.TextField()
    querylinks = models.TextField()
    queryresults = models.TextField()
    querycomments = models.TextField()
    class Meta:
        db_table = u'pga_queries'

class PgaReports(models.Model):
    reportname = models.CharField(max_length=64, primary_key=True)
    reportsource = models.TextField()
    reportbody = models.TextField()
    reportprocs = models.TextField()
    reportoptions = models.TextField()
    class Meta:
        db_table = u'pga_reports'

class PgaScripts(models.Model):
    scriptname = models.CharField(max_length=64, primary_key=True)
    scriptsource = models.TextField()
    class Meta:
        db_table = u'pga_scripts'

class Procedencia(models.Model):
    pro_id = models.IntegerField()
    pro_nombre = models.CharField(max_length=-1)
    class Meta:
        db_table = u'procedencia'

class Provincias(models.Model):
    prov_id = models.IntegerField(primary_key=True)
    prov_nombre = models.CharField(max_length=255)
    prov_fk_region = models.IntegerField()
    class Meta:
        db_table = u'provincias'

class Prueba(models.Model):
    id_per = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=-1)
    rut = models.CharField(max_length=-1)
    direccion = models.CharField(max_length=-1)
    telefono = models.IntegerField()
    class Meta:
        db_table = u'prueba'

class Recoverpassword(models.Model):
    reco_id = models.IntegerField(primary_key=True)
    reco_pregunta_one = models.CharField(max_length=200)
    reco_pregunta_two = models.CharField(max_length=200)
    reco_respuesta = models.CharField(max_length=200)
    reco_username = models.CharField(max_length=200)
    class Meta:
        db_table = u'recoverpassword'

class Regiones(models.Model):
    regi_id = models.IntegerField(primary_key=True)
    regi_nombre = models.CharField(max_length=55)
    regi_nro = models.IntegerField()
    regi_capital_fk_provincias = models.CharField(max_length=40)
    regi_nombre_reg = models.CharField(max_length=75)
    class Meta:
        db_table = u'regiones'

class Responsables(models.Model):
    cuer = models.ForeignKey(Companias)
    comp_id = models.IntegerField()
    codigo = models.CharField(max_length=40)
    rut = models.CharField(max_length=15)
    dv = models.CharField(max_length=1)
    nombres = models.CharField(max_length=256)
    apepaterno = models.CharField(max_length=256)
    apematerno = models.CharField(max_length=256)
    fechanacimiento = models.DateField()
    estadoresponsable = models.IntegerField()
    descripcion = models.CharField(max_length=256)
    class Meta:
        db_table = u'responsables'

class Situaciones(models.Model):
    situ_id = models.IntegerField(primary_key=True)
    situ_fk_idarticulo = models.IntegerField()
    situ_numero_situacion = models.IntegerField()
    situ_comentario = models.CharField(max_length=256)
    class Meta:
        db_table = u'situaciones'

class Suerper%5(models.Model):

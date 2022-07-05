from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField, IntegerField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length
class BreastCancerForm(FlaskForm):
    
    radius_mean = FloatField('radius_mean', validators=[DataRequired()])
    texture_mean = FloatField('texture_mean', validators=[DataRequired()])
    perimeter_mean = FloatField('perimeter_mean', validators=[DataRequired()])
    area_mean = FloatField('area_mean', validators=[DataRequired()])
    smoothness_mean = FloatField('smoothness_mean', validators=[DataRequired()])
    compactness_mean = FloatField('compactness_mean', validators=[DataRequired()])
    concavity_mean = FloatField('concavity_mean', validators=[DataRequired()])
    concave_points_mean = FloatField('concave_points_mean', validators=[DataRequired()])
    symmetry_mean = FloatField('symmetry_mean', validators=[DataRequired()])
    fractal_dimension_mean = FloatField('fractal_dimension_mean', validators=[DataRequired()])
    radius_se = FloatField('radius_se', validators=[DataRequired()])
    texture_se = FloatField('texture_se', validators=[DataRequired()])
    perimeter_se = FloatField('perimeter_se', validators=[DataRequired()])
    area_se = FloatField('area_se', validators=[DataRequired()])
    smoothness_se = FloatField('smoothness_se', validators=[DataRequired()])
    compactness_se = FloatField('compactness_se', validators=[DataRequired()])
    concavity_se = FloatField('concavity_se', validators=[DataRequired()])
    concave_points_se = FloatField('concave_points_se', validators=[DataRequired()])
    symmetry_se = FloatField('symmetry_se', validators=[DataRequired()])
    fractal_dimension_se = FloatField('fractal_dimension_se', validators=[DataRequired()])
    radius_worst = FloatField('radius_worst', validators=[DataRequired()])
    texture_worst = FloatField('texture_worst', validators=[DataRequired()])
    perimeter_worst = FloatField('perimeter_worst', validators=[DataRequired()])
    area_worst = FloatField('area_worst', validators=[DataRequired()])
    smoothness_worst = FloatField('smoothness_worst', validators=[DataRequired()])
    compactness_worst = FloatField('compactness_worst', validators=[DataRequired()])
    concavity_worst = FloatField('concavity_worst', validators=[DataRequired()])
    concave_points_worst = FloatField('concave_points_worst', validators=[DataRequired()])
    symmetry_worst = FloatField('symmetry_worst', validators=[DataRequired()])
    fractal_dimension_worst = FloatField('fractal_dimension_worst', validators=[DataRequired()])

    submit = SubmitField('Predict')
    #--------------------------------------------------------------------------------------------
    positiveResult = 'Prediction : Positive'
    negativeResult = 'Prediction : Negative'
    breastCancerResult = 'not yet'
    #--------------------------------------------------------------------------------------------
    def checkBreastCancer(self, radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, 
        concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, 
        area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, 
        radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, 
        concave_points_worst, symmetry_worst, fractal_dimension_worst):
        #--------------------------------------------------------------------------------------
        model = 'Model : Logistic Regression'
        return self.breastCancerResult
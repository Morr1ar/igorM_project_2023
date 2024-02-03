"""empty message

Revision ID: 72d3b38639b3
Revises: 0c16a0016dc4
Create Date: 2024-02-01 08:56:04.413264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72d3b38639b3'
down_revision = '0c16a0016dc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('codes', schema=None) as batch_op:
        batch_op.drop_index('ix_codes_code_hash')

    op.drop_table('codes')
    op.drop_table('visits')
    with op.batch_alter_table('pupils', schema=None) as batch_op:
        batch_op.add_column(sa.Column('out_time', sa.DateTime(), nullable=True))
        batch_op.drop_index('ix_pupils_last_generated_code')
        batch_op.create_index(batch_op.f('ix_pupils_last_generated_code'), ['last_generated_code'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pupils', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_pupils_last_generated_code'))
        batch_op.create_index('ix_pupils_last_generated_code', ['last_generated_code'], unique=False)
        batch_op.drop_column('out_time')

    op.create_table('visits',
    sa.Column('visit_id', sa.INTEGER(), nullable=False),
    sa.Column('pupil_id', sa.INTEGER(), nullable=True),
    sa.Column('visit_datetime', sa.DATETIME(), nullable=True),
    sa.Column('code_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['code_id'], ['codes.code_id'], ),
    sa.ForeignKeyConstraint(['pupil_id'], ['pupils.pupil_id'], ),
    sa.PrimaryKeyConstraint('visit_id')
    )
    op.create_table('codes',
    sa.Column('code_id', sa.INTEGER(), nullable=False),
    sa.Column('code_hash', sa.VARCHAR(length=2048), nullable=True),
    sa.Column('pupil_id', sa.INTEGER(), nullable=True),
    sa.Column('code_datetime', sa.DATETIME(), nullable=True),
    sa.Column('code_expire_datetime', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['pupil_id'], ['pupils.pupil_id'], ),
    sa.PrimaryKeyConstraint('code_id')
    )
    with op.batch_alter_table('codes', schema=None) as batch_op:
        batch_op.create_index('ix_codes_code_hash', ['code_hash'], unique=False)

    # ### end Alembic commands ###
import logging
import os 

# include all python script in the current directory

__all__ = [f for f in os.listdir('./app/') if f.lower().endswith('.py')
                                              and f != '__init__.py'
                                              and os.path.isfile(f)]